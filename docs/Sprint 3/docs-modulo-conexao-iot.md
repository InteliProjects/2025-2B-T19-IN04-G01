# Sprint 3 - Módulo de Conexão IoT

## Visão Geral

Na Sprint 3, foi desenvolvido um módulo completo de integração IoT que atua como ponte entre dispositivos IoT e o banco de dados Supabase. O sistema consome mensagens de telemetria através do RabbitMQ, processa os dados e os armazena de forma incremental no banco de dados PostgreSQL do Supabase, além de gerar agregações horárias para análise de rodas e bancos de veículos.

## Arquitetura e Componentes

### 1. Consumidor RabbitMQ

O módulo implementa um consumidor RabbitMQ que:

- Conecta-se ao broker configurado via variáveis de ambiente
- Processa mensagens da fila de forma sequencial (QoS = 1)
- Gerencia reconexões com heartbeat e timeout configuráveis
- Controla confirmações (ACK/NACK) para garantir processamento confiável
- Reencaminha mensagens com falha para reprocessamento

### 2. Processamento de Telemetria

O sistema processa mensagens JSON contendo dados de telemetria de veículos, incluindo:

- Identificação: PIN único do dispositivo/produto
- Informações do modelo: código do modelo, descrição, ano (MDY/SPJ)
- Estágios de produção: timestamps dos estágios M100, M200, M215, M244, M252, M282, M310, M313, G700
- Metadados: cor, país, parâmetros adicionais (PR)
- Campos temporais: published_at, scheduled_for, original_stage_timestamp

### 3. Armazenamento Incremental (UPSERT)

A função insert_telemetry implementa uma estratégia de atualização incremental:

- Novos registros: Quando um PIN não existe, cria um novo registro completo
- Atualizações: Quando o PIN já existe, atualiza apenas os campos presentes na mensagem
- Preservação de dados: Campos informativos (model, modelo, mdy, spj, cor, pais, pr) preservam valores existentes usando COALESCE
- Atualização de estágios: Timestamps de estágios são sempre atualizados quando presentes
- Timestamp de recebimento: Campo received_at é sempre atualizado com o momento do processamento

### 4. Conversão de Timestamps

O sistema converte timestamps em múltiplos formatos:

- Formato completo: 2025-11-12-03.15.27.112944 (com microssegundos)
- Formato sem microssegundos: 2025-11-12-03.15.27
- Unix timestamp: Valores numéricos são aceitos diretamente
- Armazenamento: Todos os timestamps são convertidos para Unix timestamp (inteiro) antes do armazenamento

### 5. Mapeamento de Rodas

O sistema mantém um mapeamento completo entre códigos de modelo e informações de rodas:

- MODEL_WHEEL_MAP: Dicionário que mapeia códigos de modelo para (RAD, descrição, coluna_matriz)
- Lookup tolerante: A função get_wheel_info implementa três estratégias de busca:
  1. Busca exata por código de modelo
  2. Busca por prefixo (maior prefixo correspondente)
  3. Busca por descrição (maior descrição encontrada na string)
- RADs autorizados: Lista estrita de códigos RAD permitidos (40I, 41P, 44M, 45H, 48E, C0A, C0V, C1Y, C4W, C5N, C6E, CI1, CI4, CR4, CV2, V41)

### 6. Mapeamento de Bancos

Similar ao sistema de rodas, o módulo mapeia códigos de modelo para bancos de veículos:

- BANK_CODE_MAP: Mapeia códigos de modelo para (MODELCODE, descrição, MODELCODE)
- Lookup por prefixo e descrição: A função get_bank_info_by_model busca o melhor match usando prefixo ou descrição
- Modelos suportados: Inclui modelos como Saveiro, Virtus, Nivus, Track, entre outros

### 7. Agregação Horária

O sistema gera agregações horárias em duas tabelas matriz:

#### Matriz de Rodas (wheel_hourly_matrix)
- Estrutura: Uma linha por hora (bucket_start) com colunas dinâmicas para cada RAD
- Contagem: Incrementa contadores para cada tipo de roda produzida naquela hora
- Criação automática de colunas: Colunas são criadas automaticamente conforme os RADs autorizados
- Limpeza de colunas: Remove colunas não autorizadas automaticamente

#### Matriz de Bancos (bank_hourly_matrix)
- Estrutura: Uma linha por hora com colunas dinâmicas para cada código de banco
- Contagem: Incrementa contadores para cada tipo de banco produzido naquela hora
- Criação automática de colunas: Colunas são criadas automaticamente conforme os códigos de banco mapeados

### 8. Gerenciamento de Schema

O módulo inclui funcionalidades para gerenciar o schema do banco de dados:

- Aplicação automática: A função ensure_schema aplica o schema SQL na inicialização
- Validação de colunas: Garante que todas as colunas necessárias existam nas tabelas matriz
- Limpeza automática: Remove colunas não autorizadas das tabelas matriz
- Configuração flexível: Schema e nome das tabelas configuráveis via variáveis de ambiente

## Configuração

O sistema utiliza variáveis de ambiente para todas as configurações sensíveis:

### RabbitMQ
- RABBITMQ_HOST: Host do broker RabbitMQ
- RABBITMQ_PORT: Porta do broker
- RABBITMQ_USER: Usuário para autenticação
- RABBITMQ_PASS: Senha para autenticação
- RABBITMQ_QUEUE: Nome da fila a ser consumida
- RABBITMQ_HEARTBEAT: Intervalo de heartbeat (padrão: 600s)
- RABBITMQ_BLOCKED_TIMEOUT: Timeout para conexões bloqueadas (padrão: 300s)

### Supabase
- SUPABASE_DB_URL: URL completa de conexão do PostgreSQL
- SUPABASE_SCHEMA: Schema do banco (padrão: "public")
- SCHEMA_FILE: Caminho para o arquivo SQL do schema (padrão: "schema.sql")

### Tabelas e Processamento
- DB_TABLE_NAME: Nome da tabela principal de telemetria
- STAGE_TIMESTAMP_COLUMNS: Lista de códigos de estágios que contêm timestamps (separados por vírgula)
- WHEEL_MATRIX_TABLE: Nome da tabela de matriz de rodas (padrão: "wheel_hourly_matrix")
- BANK_MATRIX_TABLE: Nome da tabela de matriz de bancos (padrão: "bank_hourly_matrix")

## Fluxo de Processamento

1. Inicialização:
   - Carrega variáveis de ambiente
   - Conecta ao Supabase
   - Aplica e valida o schema
   - Garante existência de colunas nas tabelas matriz
   - Remove colunas não autorizadas

2. Conexão RabbitMQ:
   - Estabelece conexão com o broker
   - Declara a fila
   - Configura QoS para processamento sequencial
   - Inicia consumo de mensagens

3. Processamento de Mensagem:
   - Recebe mensagem JSON da fila
   - Valida presença do PIN
   - Processa e converte campos
   - Executa UPSERT na tabela principal
   - Se for novo PIN, atualiza matrizes horárias de rodas e bancos
   - Confirma processamento (ACK) ou reencaminha (NACK)

4. Tratamento de Erros:
   - Erros de JSON: ACK (mensagem inválida é descartada)
   - Erros de processamento: NACK com requeue (mensagem é reprocessada)
   - Erros de banco: Rollback da transação

## Características Técnicas

### Segurança
- Credenciais armazenadas em variáveis de ambiente
- Nenhum dado sensível no código
- Validação de entrada (PIN obrigatório)
- Sanitização de nomes de colunas SQL

### Performance
- Processamento sequencial (evita race conditions)
- Índices no banco para consultas rápidas
- Transações otimizadas
- Agregações incrementais (UPSERT em vez de recálculo)

### Confiabilidade
- Confirmação manual de mensagens (ACK/NACK)
- Reencaminhamento de mensagens com falha
- Rollback em caso de erro
- Logs detalhados para debugging

### Manutenibilidade
- Código bem documentado
- Funções modulares e reutilizáveis
- Configuração externa (sem hardcoding)
- Tratamento robusto de erros

## Dependências

- pika: Cliente RabbitMQ para Python
- psycopg2: Driver PostgreSQL para Python
- python-dotenv: Carregamento de variáveis de ambiente

## Resultados

O módulo desenvolvido permite:

- Integração completa entre dispositivos IoT e banco de dados
- Processamento em tempo real de telemetria de produção
- Agregação automática de dados para análise
- Rastreabilidade completa do ciclo de vida dos produtos
- Escalabilidade para processar grandes volumes de mensagens
- Confiabilidade com tratamento robusto de erros e reconexões