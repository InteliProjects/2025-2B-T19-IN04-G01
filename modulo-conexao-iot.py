"""Consumidor RabbitMQ → Supabase com armazenamento em tabela única.


Este script:
1. Lê variáveis de ambiente para configurar conexões.
2. Consome mensagens JSON de uma fila RabbitMQ.
3. Converte e normaliza os dados recebidos.
4. Realiza UPSERT em uma tabela PostgreSQL (Supabase), armazenando cada PIN em linha única.
5. Mantém um resumo horário de rodas e bancos usando mapas embutidos.
"""


from __future__ import annotations


import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


import pika
import psycopg2
from dotenv import load_dotenv
from psycopg2 import extensions


# Carrega variáveis do arquivo .env (se disponível).
load_dotenv()



def get_env_var(name: str, required: bool = True) -> Optional[str]:
    """Obtem variável de ambiente (falha se ausente quando obrigatória)."""
    value = os.getenv(name)
    if required and not value:
        print(f"Variável de ambiente obrigatória não configurada: {name}")
        sys.exit(1)
    return value



def get_env_int(name: str, default: Optional[int] = None) -> int:
    """Obtém variável de ambiente como inteiro."""
    value = get_env_var(name, required=default is None)
    if value:
        try:
            return int(value)
        except ValueError:
            print(f"Variável {name} deve ser um número inteiro. Valor recebido: {value}")
            sys.exit(1)
    return default



def get_env_list(name: str, separator: str = ",") -> List[str]:
    """Obtém variável de ambiente como lista separada por vírgula."""
    value = get_env_var(name, required=True)
    return [item.strip() for item in value.split(separator) if item.strip()]



# ==================== CONFIGURAÇÃO RABBITMQ ====================
# Todas as configurações são externas (.env) para evitar dados sensíveis no código.
RABBITMQ_HOST = get_env_var("RABBITMQ_HOST")
RABBITMQ_PORT = get_env_int("RABBITMQ_PORT")
RABBITMQ_USER = get_env_var("RABBITMQ_USER")
RABBITMQ_PASS = get_env_var("RABBITMQ_PASS")
QUEUE_NAME = get_env_var("RABBITMQ_QUEUE")
RABBITMQ_HEARTBEAT = get_env_int("RABBITMQ_HEARTBEAT", default=600)
RABBITMQ_BLOCKED_TIMEOUT = get_env_int("RABBITMQ_BLOCKED_TIMEOUT", default=300)


# ==================== CONFIGURAÇÃO SUPABASE ====================
# URL completa do banco e caminhos auxiliares (schema, etc).
SUPABASE_DB_URL = get_env_var("SUPABASE_DB_URL")
SUPABASE_SCHEMA = get_env_var("SUPABASE_SCHEMA", required=False) or "public"


SCHEMA_FILE = Path("docs/Sprint 3/schema.sql")


# ==================== CONFIGURAÇÃO DE TABELA ====================
# Nome da tabela de destino e códigos de estágios que contêm timestamps.
TABLE_NAME = get_env_var("DB_TABLE_NAME")
STAGE_TIMESTAMP_COLUMNS = get_env_list("STAGE_TIMESTAMP_COLUMNS")
STAGE_TIMESTAMP_SET = {code.upper() for code in STAGE_TIMESTAMP_COLUMNS}
DATETIME_FIELDS = [field.lower() for field in STAGE_TIMESTAMP_COLUMNS] + [
    "published_at",
    "scheduled_for",
    "original_stage_timestamp",
]
DATETIME_FIELDS_SET = set(DATETIME_FIELDS)


# ==================== CONFIGURAÇÃO RESUMO DE RODAS ====================
# mapas de rodas são embutidos no código (MODEL_WHEEL_MAP);
WHEELS_PER_CAR = get_env_int("WHEELS_PER_CAR", default=4) or 4
WHEEL_MATRIX_TABLE = get_env_var("WHEEL_MATRIX_TABLE", required=False) or "wheel_hourly_matrix"


# ==================== CONFIGURAÇÃO RESUMO DE BANCOS ====================
# mapas de bancos são embutidos no código (BANK_CODE_MAP); 
BANK_MATRIX_TABLE = get_env_var("BANK_MATRIX_TABLE", required=False) or "bank_hourly_matrix"


# Lista estrita de RADs (nomes de coluna) conforme solicitado.
ALLOWED_RAD_COLUMNS = {
    "40I","41P","44M","45H","48E",
    "C0A","C0V","C1Y","C4W","C5N",
    "C6E","CI1","CI4","CR4","CV2","V41"
}



def sanitize_description_column(description: str) -> str:
    """Converte a descrição da roda em um nome de coluna seguro.
    Mantém apenas a descrição sanitizada, sem prefixo (ex: steel_wheels_5_5j_x_15).
    Substitui pontos por underscores para evitar problemas no SQL."""
    # Preserva letras, números, espaços, 'x' e 'J' (case-insensitive)
    # Substitui pontos por underscores para evitar problemas no SQL
    safe = "".join(ch.lower() if ch.isalnum() or ch in (" ", "x", "X", "J") else "_" for ch in description)
    # Remove espaços extras e converte espaços para underscore
    safe = "_".join(safe.split())
    # Remove underscores duplicados
    while "__" in safe:
        safe = safe.replace("__", "_")
    safe = safe.strip("_")
    return safe or "descricao_desconhecida"



# MODEL_WHEEL_MAP: Modell -> (RAD, DESCRIÇÃO, COLUNA_MATRIZ)
# A coluna será o RAD quando o RAD estiver em ALLOWED_RAD_COLUMNS, caso contrário None.
MODEL_WHEEL_MAP: Dict[str, Tuple[str, str, Optional[str]]] = {
    "R111Q4": ("40I", "Steel wheels 5.5J x 15", "40I"),
    "BZ42K3": ("41P", "Alloy wheels 6J x 15", "41P"),
    "BZ42T4": ("41P", "Alloy wheels 6J x 15", "41P"),
    "BZ42K4": ("41P", "Alloy wheels 6J x 15", "41P"),
    "BZ42D3": ("41P", "Alloy wheels 6J x 15", "41P"),
    "BZ47NY": ("44M", "Alloy wheels 7J x 18", "44M"),
    "BZ44BY": ("45H", "Alloy wheels 6.5J x 17", "45H"),
    "BZ44D3": ("45H", "Alloy wheels 6.5J x 17", "45H"),
    "CH29NY": ("C4W", "Alloy wheels 6.5J x 17", "C4W"),
    "CH23BY": ("C1Y", "Alloy wheels 6J x 16", "C1Y"),
    "CH23K3": ("C1Y", "Alloy wheels 6J x 16", "C1Y"),
    "BZ4AK4": ("C0V", "Steel wheels 6J x 15", "C0V"),
    "CH22K3": ("C1Y", "Alloy wheels 6J x 16", "C1Y"),
    "CH23R4": ("C1Y", "Alloy wheels 6J x 16", "C1Y"),
    "CH24BY": ("CI4", "Alloy wheels 6.5J x 17", "CI4"),
    "CH24K3": ("CI4", "Alloy wheels 6.5J x 17", "CI4"),
    "CH21BY": ("C5N", "Steel wheels 6J x 16", "C5N"),
    "5URNT4": ("C6E", "Steel wheels 6J x 15", "C6E"),
    "5URNU4": ("C6E", "Steel wheels 6J x 15", "C6E"),
    "5UKNU4": ("C6E", "Steel wheels 6J x 15", "C6E"),
    "5UKWT4": ("CR4", "Alloy wheels 6J x 15", "CR4"),
    "5URTU4": ("CR4", "Alloy wheels 6J x 15", "CR4"),
    "5URTT4": ("CR4", "Alloy wheels 6J x 15", "CR4"),
    "BZ39NY": ("CI1", "Alloy wheels 7J x 18", "CI1"),
    "BZ43BY": ("CV2", "Alloy wheels 6J x 16", "CV2"),
    "BZ43D3": ("CV2", "Alloy wheels 6J x 16", "CV2"),
    "BZ43P3": ("CV2", "Alloy wheels 6J x 16", "CV2"),
    "5UK8U4": ("V41", "Alloy wheels 6J x 15", "V41"),
    "5UK8T4": ("V41", "Alloy wheels 6J x 15", "V41"),
}


# Ajusta coluna para None se RAD não estiver na lista autorizada
for k, (rad, desc, col) in list(MODEL_WHEEL_MAP.items()):
    if rad not in ALLOWED_RAD_COLUMNS:
        MODEL_WHEEL_MAP[k] = (rad, desc, None)


# --- ADICIONADO: mapa RAD -> coluna usado pelas funções que garantem/atualizam colunas ---
RAD_COLUMN_MAP: Dict[str, str] = {}
for (_, (rad, _, col)) in MODEL_WHEEL_MAP.items():
    if rad and rad in ALLOWED_RAD_COLUMNS:
        # usa o RAD exatamente como nome de coluna
        RAD_COLUMN_MAP[rad] = rad
# --- ADICIONAR: função de lookup tolerante para rodas (após MODEL_WHEEL_MAP) ---
def get_wheel_info(model_code: Optional[str]) -> Optional[Tuple[str, str, Optional[str]]]:
    """Retorna (RAD, descrição, coluna) para o modelo informado.
    Estratégia:
      1) lookup exato por chave em MODEL_WHEEL_MAP
      2) maior prefix match (ex.: incoming '5URT...' encontra chave '5URT')
      3) match por descrição (maior descrição presente na string)
    """
    if not model_code:
        return None
    s = model_code.strip().upper()


    # 1) lookup exato
    exact = MODEL_WHEEL_MAP.get(s)
    if exact:
        return exact


    # 2) maior prefix match
    best_key = None
    for key in MODEL_WHEEL_MAP.keys():
        if key and s.startswith(key):
            if best_key is None or len(key) > len(best_key):
                best_key = key
    if best_key:
        return MODEL_WHEEL_MAP[best_key]


    # 3) match por descrição (maior descrição encontrada)
    best_desc = None
    best_val = None
    for _, (rad, desc, col) in MODEL_WHEEL_MAP.items():
        if desc and desc.upper() in s:
            if best_desc is None or len(desc) > len(best_desc):
                best_desc = desc
                best_val = (rad, desc, col)
    if best_val:
        return best_val


    return None


# BANK_CODE_MAP: MODELCODE -> (MODELCODE, DESC, MODELCODE)
BANK_CODE_MAP: Dict[str, Tuple[str, str, str]] = {
    "5UK8": ("5UK8", "Saveiro3G  CDExtrePA", "5UK8"),
    "5UKN": ("5UKN", "_+", "5UKN"),
    "5UKW": ("5UKW", "Saveiro3G  CDCOMF PA", "5UKW"),
    "5URN": ("5URN", "Saveiro3TF CSRobusPA", "5URN"),
    "5URT": ("5URT", "Saveiro3G  CSTrendPA", "5URT"),
    "BZ42": ("BZ42", "VIRTUS 1.0 PALINE1", "BZ42"),
    "BZ43": ("BZ43", "VIRTUS 1.0 PALINE2 / PACOMFO", "BZ43"),
    "BZ44": ("BZ44", "VIRTUS 1,0 PAHIGHL", "BZ44"),
    "BZ4A": ("BZ4A", "VIRTUS 1.0 PASENSE", "BZ4A"),
    "CH21": ("CH21", "NIVUS  1.0 PASENSE", "CH21"),
    "CH22": ("CH22", "NIVUS  1.0 PAENTRY", "CH22"),
    "CH23": ("CH23", "NIVUS  1.0 PACOMFO", "CH23"),
    "CH24": ("CH24", "NIVUS  1.0 PAHIGH", "CH24"),
    "CH29": ("CH29", "NIVUS  1.4 PAGTS", "CH29"),
    "R111": ("R111", "Track  1.0", "R111"),
}


# BANK_DESC_MAP: description_upper -> MODELCODE (para matching por descrição)
BANK_DESC_MAP: Dict[str, str] = {desc.upper(): code for code, (_, desc, _) in BANK_CODE_MAP.items() if desc}



def bucket_start_from_epoch(epoch_seconds: int) -> datetime:
    """Trunca o timestamp Unix para o início da hora (UTC)."""
    dt = datetime.fromtimestamp(epoch_seconds, tz=timezone.utc)
    return dt.replace(minute=0, second=0, microsecond=0)



def upsert_hourly_wheel_matrix(
    cursor: extensions.cursor,
    bucket_start: datetime,
    column_name: str,
) -> None:
    """Incrementa a contagem da roda específica na tabela matriz."""
    # Usa aspas duplas para escapar o nome da coluna (necessário para caracteres especiais)
    cursor.execute(
        f"""
        INSERT INTO {WHEEL_MATRIX_TABLE} (bucket_start, "{column_name}", updated_at)
        VALUES (%s, 1, NOW())
        ON CONFLICT (bucket_start) DO UPDATE SET
            "{column_name}" = {WHEEL_MATRIX_TABLE}."{column_name}" + 1,
            updated_at = NOW()
        """,
        (bucket_start,),
    )


def get_bank_info_by_model(model_str: Optional[str]) -> Optional[Tuple[str, str]]:
    """
    Tenta extrair o banco a partir do model recebido na fila.
    Retorna (MODELCODE, desc_or_match) ou None.
    """
    if not model_str:
        return None
    s = model_str.strip().upper()


    # 1) tenta casar por MODELCODE prefixo (maior prefixo)
    best_code = None
    for code in BANK_CODE_MAP.keys():
        if code and s.startswith(code):
            if best_code is None or len(code) > len(best_code):
                best_code = code
    if best_code:
        _, desc, col = BANK_CODE_MAP[best_code]
        return col, desc


    # 2) tenta casar pela descrição: pega o maior DESC que esteja dentro da string recebida
    best_desc = None
    for desc_upper, model_code in BANK_DESC_MAP.items():
        if desc_upper in s:
            if best_desc is None or len(desc_upper) > len(best_desc):
                best_desc = desc_upper
    if best_desc:
        return BANK_DESC_MAP[best_desc], best_desc


    return None



def upsert_hourly_bank_matrix(
    cursor: extensions.cursor,
    bucket_start: datetime,
    column_name: str,
) -> None:
    """Incrementa a contagem do banco específico na tabela matriz de bancos."""
    cursor.execute(
        f"""
        INSERT INTO {BANK_MATRIX_TABLE} (bucket_start, "{column_name}", updated_at)
        VALUES (%s, 1, NOW())
        ON CONFLICT (bucket_start) DO UPDATE SET
            "{column_name}" = {BANK_MATRIX_TABLE}."{column_name}" + 1,
            updated_at = NOW()
        """,
        (bucket_start,),
    )


def ensure_schema(conn: extensions.connection) -> None:
    """Aplica schema SQL."""
    if not SCHEMA_FILE.exists():
        raise FileNotFoundError(f"Arquivo de schema não encontrado: {SCHEMA_FILE}")

    schema_sql = SCHEMA_FILE.read_text(encoding="utf-8")
    statements = [stmt.strip() for stmt in schema_sql.split(";") if stmt.strip()]


    with conn.cursor() as cursor:
        for statement in statements:
            if statement:
                cursor.execute(statement)
    conn.commit()
    print("Schema validado no Supabase")



def ensure_wheel_matrix_columns(conn: extensions.connection) -> None:
    """Cria colunas de rodas permitidas."""
    if not RAD_COLUMN_MAP:
        return
    with conn.cursor() as cursor:
        for column in RAD_COLUMN_MAP.values():
            cursor.execute(
                f"""
                ALTER TABLE {WHEEL_MATRIX_TABLE}
                ADD COLUMN IF NOT EXISTS "{column}" INTEGER NOT NULL DEFAULT 0
                """
            )
    conn.commit()



def prune_wheel_matrix_columns(conn: extensions.connection) -> None:
    """Remove colunas inválidas da matriz de rodas."""
    keep_columns = { "bucket_start", "updated_at" } | set(ALLOWED_RAD_COLUMNS)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = %s AND table_name = %s
                """,
                (SUPABASE_SCHEMA, WHEEL_MATRIX_TABLE)
            )
            existing = [row[0] for row in cursor.fetchall()]


            for col in existing:
                if col not in keep_columns:
                    print(f"Removendo coluna não autorizada: {col}")
                    cursor.execute(f'ALTER TABLE {WHEEL_MATRIX_TABLE} DROP COLUMN IF EXISTS "{col}"')
        conn.commit()
    except Exception as e:
        print(f"Falha ao limpar colunas da tabela {WHEEL_MATRIX_TABLE}: {e}")
        conn.rollback()


def ensure_bank_matrix_columns(conn: extensions.connection) -> None:
    """Garante existência das colunas na tabela de matriz de bancos usando MODELCODE como nomes."""
    if not BANK_CODE_MAP:
        return
    with conn.cursor() as cursor:
        for column in sorted(BANK_CODE_MAP.keys()):
            cursor.execute(
                f"""
                ALTER TABLE {BANK_MATRIX_TABLE}
                ADD COLUMN IF NOT EXISTS "{column}" INTEGER NOT NULL DEFAULT 0
                """
            )
    conn.commit()


def prune_bank_matrix_columns(conn: extensions.connection) -> None:
    """Remove colunas inválidas da matriz de bancos."""
    keep_columns = {"bucket_start", "updated_at"} | set(BANK_CODE_MAP.keys())
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = %s AND table_name = %s
                """,
                (SUPABASE_SCHEMA, BANK_MATRIX_TABLE)
            )
            existing = [row[0] for row in cursor.fetchall()]
            for col in existing:
                if col not in keep_columns:
                    print(f"Removendo coluna não autorizada da matriz de bancos: {col}")
                    cursor.execute(f'ALTER TABLE {BANK_MATRIX_TABLE} DROP COLUMN IF EXISTS "{col}"')
        conn.commit()
    except Exception as e:
        print(f"Falha ao limpar colunas da tabela {BANK_MATRIX_TABLE}: {e}")
        conn.rollback()


def parse_timestamp(ts_str: Any) -> Optional[int]:
    """
    Converte string do tipo '2025-11-12-03.15.27.112944' para Unix timestamp (int)
    """
    if ts_str in (None, ""):
        return None
    
    if isinstance(ts_str, (int, float)):
        return int(ts_str)
    
    try:
        # Formato completo com microssegundos.
        dt = datetime.strptime(str(ts_str), "%Y-%m-%d-%H.%M.%S.%f")
        return int(dt.timestamp())
    except (ValueError, TypeError):
        try:
            # Formato sem microssegundos.
            dt = datetime.strptime(str(ts_str), "%Y-%m-%d-%H.%M.%S")
            return int(dt.timestamp())
        except (ValueError, TypeError):
            return None



def insert_telemetry(conn: extensions.connection, message: Dict[str, Any]) -> bool:
    """
    Insere ou atualiza telemetria no Supabase de forma incremental.
    Se o PIN já existe, atualiza apenas os campos presentes na mensagem.
    Se o PIN não existe, cria um novo registro e atualiza o resumo horário de rodas.
    """
    try:
        cursor = conn.cursor()


        # Extrai PIN da mensagem (obrigatório)
        pin = message.get("PIN") or message.get("pin")
        if not pin:
            print("Mensagem sem PIN, ignorando...")
            return False


        # Processa campos da mensagem
        data_to_insert: Dict[str, Any] = {"pin": pin}
        update_clauses: List[str] = []
        
        # Processa todos os campos da mensagem
        for k, v in message.items():
            key_lower = k.lower()
            
            # Ignora PIN (já processado) e campos vazios
            if key_lower == "pin" or v is None or v == "":
                continue
            
            if k.upper() in STAGE_TIMESTAMP_SET or key_lower in DATETIME_FIELDS_SET:
                # Converte timestamps (estágios ou campos temporais adicionais) para Unix timestamp (int)
                timestamp_value = parse_timestamp(v)
                if timestamp_value is not None:
                    data_to_insert[key_lower] = timestamp_value
                    # Atualiza campo temporal apenas se vier um novo valor (não sobrescreve com NULL)
                    update_clauses.append(f"{key_lower} = EXCLUDED.{key_lower}")
            else:
                # Mantém outros campos como estão
                data_to_insert[key_lower] = v
                # Para campos informativos, preserva valor existente se já existir, senão usa o novo
                if key_lower in ["model", "modelo", "mdy", "spj", "cor", "pais", "pr"]:
                    # Preserva valor existente, usa novo apenas se não existir
                    update_clauses.append(f"{key_lower} = COALESCE({TABLE_NAME}.{key_lower}, EXCLUDED.{key_lower})")
                elif key_lower == "stage":
                    update_clauses.append(f"{key_lower} = EXCLUDED.{key_lower}")


        # Adiciona timestamp de recebimento (sempre atualiza)
        data_to_insert["received_at"] = int(time.time())
        update_clauses.append("received_at = EXCLUDED.received_at")


        # Verifica se já existe registro para o PIN (para log informativo)
        cursor.execute(f"SELECT id FROM {TABLE_NAME} WHERE pin = %s", (pin,))
        existing_record = cursor.fetchone()
        record_exists = existing_record is not None


        # Constrói lista de colunas e valores
        columns = list(data_to_insert.keys())
        placeholders = ", ".join([f"%({col})s" for col in columns])
        columns_str = ", ".join(columns)
        
        # Constrói cláusula de UPDATE (atualiza apenas campos presentes)
        update_str = ", ".join(update_clauses) if update_clauses else "received_at = EXCLUDED.received_at"


        # UPSERT: INSERT se não existe, UPDATE se existe (baseado no PIN)
        cursor.execute(f"""
            INSERT INTO {TABLE_NAME} ({columns_str})
            VALUES ({placeholders})
            ON CONFLICT (pin) DO UPDATE SET
                {update_str}
            RETURNING id
        """, data_to_insert)


        result = cursor.fetchone()
        record_id = result[0] if result else None


        # Se for um novo PIN, registrar na tabela de matriz de rodas (caso haja mapeamento)
        if not record_exists:
            model_code = data_to_insert.get("model") or message.get("MODEL") or message.get("model")
            wheel_info = get_wheel_info(model_code) if MODEL_WHEEL_MAP else None
            if wheel_info:
                rad_code, description, column_name = wheel_info
                try:
                    bucket_epoch = data_to_insert["received_at"]
                    if column_name:
                        upsert_hourly_wheel_matrix(
                            cursor=cursor,
                            bucket_start=bucket_start_from_epoch(bucket_epoch),
                            column_name=column_name,
                        )
                except Exception as wheel_error:
                    print(f"Falha ao atualizar resumo de rodas: {wheel_error}")
            else:
                if model_code:
                    print(f"Modelo '{model_code}' sem mapeamento de rodas.")
                else:
                    print("Mensagem sem campo de modelo; resumo de rodas não atualizado.")


            # contabiliza banco
            try:
                bank_info = get_bank_info_by_model(model_code)
                if bank_info:
                    bank_col, bank_desc = bank_info
                    upsert_hourly_bank_matrix(
                        cursor=cursor,
                        bucket_start=bucket_start_from_epoch(bucket_epoch),
                        column_name=bank_col,
                    )
                    print(f"Contabilizado banco '{bank_desc}' na coluna '{bank_col}'")
                else:
                    print("Nenhum mapeamento de banco encontrado para este modelo.")
            except Exception as bank_error:
                print(f"Falha ao atualizar matriz de bancos: {bank_error}")


        conn.commit()
        cursor.close()


        if record_exists:
            print(f"PIN {pin} atualizado.")
        else:
            print(f"Novo PIN {pin} registrado (id {record_id}).")


        return True


    except Exception as e:
        print(f"Erro ao inserir/atualizar no Supabase: {e}")
        conn.rollback()
        return False



# ==================== CALLBACK PARA MENSAGENS ====================
def process_message(
    ch: pika.adapters.blocking_connection.BlockingChannel,
    method: pika.spec.Basic.Deliver,
    properties: pika.spec.BasicProperties,
    body: bytes,
    db_conn: extensions.connection,
) -> None:
    """Processa mensagens e controla ACK/NACK."""
    try:
        # Verifica se a conexão ainda está aberta antes de processar
        if db_conn is None or db_conn.closed != 0:
            print("Conexão com o banco já está fechada. Ignorando mensagem.")
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
            return

        message = json.loads(body.decode())
        print(f"\nMensagem recebida na fila '{QUEUE_NAME}':")
        print(f"   {json.dumps(message, indent=2)}")

        success = insert_telemetry(db_conn, message)

        if success:
            ch.basic_ack(delivery_tag=method.delivery_tag)
            print("Mensagem processada")
        else:
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
            print("Mensagem rejeitada e reencaminhada")

    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)



# ==================== MAIN ====================
def main():
    print("Iniciando consumidor RabbitMQ → Supabase")
    print(f"Fila: {QUEUE_NAME}")
    print(f"Broker: {RABBITMQ_HOST}:{RABBITMQ_PORT}")
    print(f"Database: Supabase PostgreSQL\n")


    db_conn = get_db_connection()
    if not db_conn:
        print("Não foi possível conectar no Supabase. Encerrando...")
        return


    try:
        ensure_schema(db_conn)
        prune_wheel_matrix_columns(db_conn)
        ensure_wheel_matrix_columns(db_conn)
        prune_bank_matrix_columns(db_conn)
        ensure_bank_matrix_columns(db_conn)
    except Exception as e:
        print(f"Falha ao aplicar schema: {e}")
        db_conn.close()
        return


    connection: Optional[pika.BlockingConnection] = None


    try:
        # Conectar no RabbitMQ
        credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=RABBITMQ_HOST,
                port=RABBITMQ_PORT,
                credentials=credentials,
                heartbeat=RABBITMQ_HEARTBEAT,
                blocked_connection_timeout=RABBITMQ_BLOCKED_TIMEOUT
            )
        )


        channel = connection.channel()
        channel.queue_declare(queue=QUEUE_NAME, durable=True)
        # Configurar QoS para processar apenas uma mensagem por vez.
        channel.basic_qos(prefetch_count=1)


        # Configurar consumidor
        channel.basic_consume(
            queue=QUEUE_NAME,
            on_message_callback=lambda ch, method, properties, body: process_message(
                ch, method, properties, body, db_conn
            ),
            auto_ack=False  # Mantém confirmação manual para controle de reprocessamento.
        )


        print("Conectado ao RabbitMQ")
        print(f"Aguardando mensagens na fila '{QUEUE_NAME}'...")
        print("   Pressione CTRL+C para sair.\n")


        # Iniciar consumo
        channel.start_consuming()


    except KeyboardInterrupt:
        print("Encerrando consumidor...")
    except Exception as e:
        print(f"Erro na conexão RabbitMQ: {e}")
    finally:
        if db_conn:
            db_conn.close()
            print("Conexão Supabase fechada")
        if connection and connection.is_open:
            connection.close()
            print("Conexão RabbitMQ fechada")



def get_db_connection() -> Optional[extensions.connection]:
    """Cria conexão com o Supabase e seta o schema."""
    try:
        conn = psycopg2.connect(SUPABASE_DB_URL)
        with conn.cursor() as cur:
            cur.execute(f"SET search_path TO {SUPABASE_SCHEMA};")
        print(f"Conectado ao Supabase PostgreSQL (schema {SUPABASE_SCHEMA})")
        return conn
    except Exception as e:
        print(f"Erro ao conectar no Supabase: {e}")
        return None



if __name__ == "__main__":
    main()