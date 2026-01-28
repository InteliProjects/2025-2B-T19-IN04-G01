# Dashboard Refinado de Monitoramento
## Solução de Internet das Coisas para Automação Sustentável - Monitoramento de Consumo de Rodas e Bancos

**Time Sem Parar**  
**Módulo: Administração Tech - IN04**  
**Parceiro: Volkswagen do Brasil**  
**Data:** Dezembro de 2025

---

## Sumário

1. [Introdução](#1-introdução)
2. [Instruções para uso do Dashboard](#2-instruções-para-uso-do-dashboard)
3. [Entendimento das funcionalidades e configuração do Dashboard](#3-entendimento-das-funcionalidades-e-configuração-do-dashboard)
4. [Conclusão](#4-conclusão)

---

## 1. Introdução

Fazendo jus ao nome da equipe, o dashboard da *Sem Parar* foi projetado pensando em maneiras de facilitar o monitoramento do consumo de rodas e bancos na linha de produção, de modo a evitar quaisquer interrupções devido à falha no alinhamento entre o consumo real e o previsto. 
Sabendo que a agilidade na tomada de decisão é crucial para manter a eficiência operacional, o dashboard foi cuidadosamente arquitetado olhando para o usuário final, que são os gestores e operadores da linha de produção, que lidam com uma quntidade enorme de dados diariamenete e por isso, precisam de uma ferramenta que seja intuitiva a ponto de permitir que as informações relevantes sejam interpretadas em poucos segundos e sem muito esforço cognitivo. 
O dashboard permite tanto uma vizualização geral do consumo, quanto uma análise detalhada por tipo de peça, possibilitando identificar rapidamente quaisquer desvios entre o consumo real e o previsto, além de destacar áreas que necessitam de atenção imediata. Foram também configurados alertas para que o usuário não deixe passar despercebido quando os limites críticos forem atingidos. 

## 2. Instruções para uso do Dashboard

O dashboard se baseia em uma arquitetura orientada a eventos, representada pelo seguinte fluxo:

**Sensores / Eventos → Fila (RabbitMQ) → Python → PostgreSQL → Grafana**

Cada componente tem um papel específico:
- A fila garante resiliência e desacoplamento;
- O script Python processa e valida os dados;
- O banco de dados organiza as informações para consulta eficiente;
- O Grafana consome os dados já tratados e agregados.

#### 2.1 Conexão com a Fila (RabbitMQ)

A fila RabbitMQ atua como o ponto central de entrada dos eventos da linha de produção.  
Nenhum dado é enviado diretamente ao banco:tudo passa primeiro pela fila.

Isso garante que:
- Eventos não sejam perdidos;
- O sistema suporte picos de mensagens;
- O processamento possa ser pausado ou reiniciado sem impacto nos sensores.

**Antes de rodar o sistema, é necessário:**

- RabbitMQ Server
- Python 3.10 ou superior
- Acesso à fila configurada (host, porta, usuário e senha)

**Funcionamento prático:**

Os sensores e sistemas da linha publicam mensagens na fila.  
Cada mensagem representa um evento de telemetria, contendo informações como:

- Identificação do veículo ou componente (`pin`);
- Modelo do carro;
- Estágio da linha de produção;
- Timestamps associados a cada etapa.

Do ponto de vista do usuário, não é necessário interagir manualmente com a fila.  
Ela deve apenas estar ativa e acessível para o script Python consumidor.

#### 2.2 Execução do Script Python

O script Python `modulo-conexao-iot.py` localizado na pasta `src`é responsável por ligar a fila ao banco de dados.

Ele executa continuamente as seguintes ações:

1. Conecta-se ao RabbitMQ;
2. Consome mensagens da fila;
3. Interpreta e valida os dados recebidos;
4. Insere os dados no PostgreSQL.

**Dependências:**

Bibliotecas utilizadas pelo script de ingestão:

- Conexão com RabbitMQ: `pika`
- Conexão com PostgreSQL:`psycopg2`
- Gerenciamento de variáveis de ambiente: `python-dotenv`

Essas dependências garantem comunicação segura com a fila, persistência no banco de dados e separação adequada de credenciais.

**Configuração do ambiente:**

O script utiliza **variáveis de ambiente** para realizar a conexão tanto com a fila RabbitMQ quanto com o banco de dados PostgreSQL.

Antes de executar o sistema, certifique-se de configurar corretamente:

**Configuração do Arquivo `.env`**

Para que o script Python funcione corretamente, é obrigatória a criação de um arquivo `.env` na raiz do projeto.  
Esse arquivo é responsável por armazenar todas as configurações sensíveis de conexão, evitando a exposição de credenciais diretamente no código.

Crie um arquivo chamado `.env` e preencha-o seguindo a estrutura abaixo, substituindo os valores pelos correspondentes ao seu ambiente:

```env
# ==================== CONFIGURAÇÃO RABBITMQ ====================

# Host do servidor RabbitMQ
RABBITMQ_HOST=SEU_HOST_AQUI

# Porta do servidor RabbitMQ (padrão: 5672)
RABBITMQ_PORT=5672

# Usuário para autenticação no RabbitMQ
RABBITMQ_USER=SEU_USUARIO

# Senha para autenticação no RabbitMQ
RABBITMQ_PASS=SUA_SENHA

# Nome da fila RabbitMQ para consumir mensagens
RABBITMQ_QUEUE=NOME_DA_FILA

# Intervalo de heartbeat em segundos
RABBITMQ_HEARTBEAT=600

# Timeout para conexão bloqueada em segundos
RABBITMQ_BLOCKED_TIMEOUT=300


# ==================== CONFIGURAÇÃO DO BANCO DE DADOS ====================

# URL completa de conexão com o PostgreSQL
# Formato: postgresql://user:password@host:port/database
SUPABASE_DB_URL=POSTGRESQL_CONNECTION_STRING

# Schema do banco de dados (padrão: public)
SUPABASE_SCHEMA=public

# Caminho para o arquivo de schema SQL
SCHEMA_FILE=schema.sql


# ==================== CONFIGURAÇÃO DE TABELA ====================

# Nome da tabela onde os dados serão inseridos
DB_TABLE_NAME=telemetry_professor

# Colunas que contêm timestamps de estágios (separadas por vírgula)
# Essas colunas serão convertidas para Unix timestamp (int) durante o processamento
STAGE_TIMESTAMP_COLUMNS=M100,M200,M215,M244,M252,M282,M310,M313,G700

```


No diretório raiz do projeto, execute:

```bash
python modulo-conexao-iot.py
```

Após iniciado, o script:

- Passa a escutar continuamente a fila RabbitMQ;
- Processa automaticamente novos eventos recebidos;
- Não requer intervenção manual durante a operação normal.



**Como Validar se Está Funcionando:**

Para confirmar que o sistema está operando corretamente:

- Verifique se novas linhas estão sendo inseridas na tabela de telemetria;
- Observe se a fila começa a esvaziar após o processamento;
- Confirme que não há erros de conexão ou exceções no terminal.

## 3. Entendimento das funcionalidades e configuração do Dashboard

A seguir, descrevemos sobre a utilização e interpretação de cada componente do dashboard desenvolvido. Serão apresentados filtros, alertas, gráficos e indicadores, detalhando a função de cada um e como eles contribuem para o monitoramento eficaz do consumo de rodas e bancos na linha de produção.

#### 3.1 Monitoramento da demanda total de bancos na linha de produção

<div align="center">
<sub>Figura 1 - Monitoramento da demanda total de bancos</sub>
</div>
<div align="center">
<img src="../../assets/monitoramento_demanda_total.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

Esta é a seção inicial e mais relevante do dashboard, projetada para oferecer uma visão rápida e consolidada do estado atual da linha de produção em relação ao consumo de bancos. Ela foi definida como a visualização inicial por concentrar, em um único painel, as informações essenciais para a tomada de decisão operacional, permitindo que o usuário compreenda o cenário geral antes de avançar para análises mais detalhadas.


Em um ambiente industrial, decisões precisam ser tomadas de forma ágil. Esta seção permite responder rapidamente a perguntas-chave, como:

- Qual é a demanda atual de bancos na linha;
- Se o consumo real está alinhado com a previsão;
- Como o consumo tem evoluído ao longo do tempo;
- Se existem indícios de risco operacional no curto prazo.


#### Indicadores principais:

#### 3.1.1 Demanda Atual da linha

<div align="center">
<sub>Figura 2 - Demanda Atual da linha</sub>
</div>
<div align="center">
<img src="../../assets/demanda_atual_linha.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

Objetivo: mostrar o consumo (demanda) de bancos por dia, consolidando todos os tipos de bancos registrados na tabela `bank_hourly_matrix`. O painel utiliza o valor do dia atual (ou o mais recente, dependendo da configuração do painel no Grafana).


```sql
SELECT
    date_trunc('day', bucket_start) AS dia,
    SUM(
        "5UK8" +
        "5UKN" +
        "5UKW" +
        "5URN" +
        "5URT" +
        "BZ42" +
        "BZ43" +
        "BZ44" +
        "BZ4A" +
        "CH21" +
        "CH22" +
        "CH23" +
        "CH24" +
        "CH29" +
        "R111"
    ) AS bancos_consumidos_dia
FROM public.bank_hourly_matrix
WHERE bucket_start >= now() - interval '7 days'
GROUP BY 1
ORDER BY dia;
```
**Como o cálculo é feito:**

- Converte o campo `bucket_start` para o nível diário utilizando `date_trunc('day', bucket_start)`, definindo o agrupamento como `dia`;
- Soma, dentro de cada dia, todas as colunas que representam os diferentes tipos de bancos (cada coluna corresponde a um tipo específico);
- Aplica um filtro temporal para considerar apenas os últimos 7 dias de dados, por meio da condição `bucket_start >= now() - interval '7 days'`;
- Agrupa os registros por `dia` e ordena o resultado de forma cronológica para facilitar a análise da evolução do consumo.

#### 3.1.2 Previsão de demanda diária:

<div align="center">
<sub>Figura 3 - Previsão de demanda diária</sub>
</div>
<div align="center">
<img src="../../assets/previsao_demanda_diaria.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

**Objetivo:** estimar uma previsão de consumo diário de bancos com base na média móvel dos últimos 14 dias completos (exclui o dia atual para evitar distorção por dados parciais).



```sql

WITH consumo_diario AS (
    SELECT
        date_trunc('day', bucket_start) AS dia,
        SUM(
            "5UK8" + "5UKN" + "5UKW" + "5URN" + "5URT" +
            "BZ42" + "BZ43" + "BZ44" + "BZ4A" +
            "CH21" + "CH22" + "CH23" + "CH24" +
            "CH29" + "R111"
        ) AS bancos_consumidos_dia
    FROM public.bank_hourly_matrix
    WHERE bucket_start >= date_trunc('day', now()) - interval '15 days'
      AND bucket_start <  date_trunc('day', now())
    GROUP BY 1
),

ultimos_14_dias AS (
    SELECT
        bancos_consumidos_dia
    FROM consumo_diario
    WHERE dia >= date_trunc('day', now()) - interval '14 days'
      AND dia <  date_trunc('day', now())
)

SELECT
    ROUND(AVG(bancos_consumidos_dia)::numeric, 2) AS previsao_diaria_mm_14d
FROM ultimos_14_dias;


```

**Como o cálculo é feito**

 `consumo_diario`

- Agrega os dados no nível diário utilizando `date_trunc('day', bucket_start)`;
- Soma todas as colunas que representam os diferentes tipos de bancos para obter o valor `bancos_consumidos_dia`;
- Aplica um filtro temporal mais amplo, considerando 15 dias e excluindo o dia atual, por meio das condições:
  - `bucket_start >= date_trunc('day', now()) - interval '15 days'`
  - `bucket_start < date_trunc('day', now())`

 `ultimos_14_dias`

- Seleciona apenas os valores diários que pertencem à janela exata dos últimos 14 dias completos, utilizando:
  - `dia >= date_trunc('day', now()) - interval '14 days'`
  - `dia < date_trunc('day', now())`

Consulta final

- Calcula a média dos valores de `bancos_consumidos_dia` dentro da janela de 14 dias;
- Arredonda o resultado para duas casas decimais utilizando `ROUND(..., 2)`.


**Por que utilizar média móvel:** A média móvel dos últimos 14 dias é utilizada como previsão de demanda diária por oferecer um equilíbrio entre estabilidade e aderência ao comportamento real da linha de produção. Ao considerar um histórico recente suficientemente amplo, o cálculo reduz o impacto de variações pontuais ou atípicas do consumo diário, resultando em um valor mais representativo do padrão operacional. A exclusão do dia atual evita distorções causadas por dados ainda incompletos, garantindo que apenas dias fechados sejam considerados. O uso de um intervalo ligeiramente maior no filtro inicial assegura consistência na janela final de cálculo. Dessa forma, a média móvel se mostra uma abordagem simples, transparente e adequada para servir como referência de comparação, especialmente em indicadores como a relação entre consumo real e previsto.

#### 3.1.3 Relação demanda real vs prevista (%)

<div align="center">
<sub>Figura 4 - Relação demanda real vs prevista (%)</sub>
</div>
<div align="center">
<img src="../../assets/relacao_demanda_prevista.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

Este gráfico tem como objetivo mostrar a relação percentual entre a demanda real de bancos na linha de produção e a demanda prevista. O indicador é construído a partir da razão entre o consumo real observado no dia e o valor de previsão diária, sendo expresso em percentual. Dessa forma, ele permite avaliar rapidamente se a operação está operando dentro do esperado. Quando o indicador atinge 90%, o gráfico assume coloração de alerta (amarelo), sinalizando que o consumo está elevado e próximo do limite esperado. Ao atingir ou ultrapassar 100%, o indicador evidencia um cenário de consumo excessivo, indicando que a linha está operando acima da capacidade planejada.

```sql

WITH consumo_diario AS (
    SELECT
        date_trunc('day', bucket_start) AS dia,
        SUM(
            "40I" + "41P" + "44M" + "45H" + "48E" +
            "C0A" + "C0V" + "C1Y" + "C4W" + "C5N" +
            "C6E" + "CI1" + "CI4" + "CR4" + "CV2" + "V41"
        ) AS rodas_consumidas_dia
    FROM public.wheel_hourly_matrix
    WHERE bucket_start >= now() - interval '30 days'
    GROUP BY 1
),

previsao_mm_14d AS (
    SELECT
        AVG(rodas_consumidas_dia) AS previsao_mm_14d
    FROM (
        SELECT rodas_consumidas_dia
        FROM consumo_diario
        ORDER BY dia DESC
        LIMIT 14
    ) t
)

SELECT
    ROUND(
        (
            (SELECT rodas_consumidas_dia
             FROM consumo_diario
             ORDER BY dia DESC
             LIMIT 1
            )
            /
            NULLIF((SELECT previsao_mm_14d FROM previsao_mm_14d), 0)
        ) * 100
    , 2);


```

**Como é calculado**


- Para cada dia, todas as colunas que representam os diferentes tipos de rodas são somadas, resultando no total diário de `rodas_consumidas_dia`;
- Considera-se um histórico dos últimos 30 dias para garantir base suficiente de dados para o cálculo da previsão;
- A previsão diária é obtida por meio de uma média móvel simples dos 14 dias mais recentes, calculada na CTE `previsao_mm_14d`;
- O consumo do dia mais recente é então dividido pelo valor da previsão, gerando uma razão entre consumo real e consumo esperado;
- O resultado é convertido em percentual, com proteção contra divisão por zero (`NULLIF`), e arredondado para duas casas decimais.

#### 3.1.4 Evolução do consumo diário de bancos

<div align="center">
<sub>Figura 5 - Evolução do consumo diário de bancos</sub>
</div>
<div align="center">
<img src="../../assets/evolucao_consumo_diario.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

Este gráfico representa a evolução diária do consumo total de bancos na linha de produção, permitindo visualizar como a demanda se comporta ao longo do tempo. Cada ponto da série corresponde ao total de bancos consumidos em um dia, consolidando todos os tipos registrados na linha. A principal função dessa visualização é contextualizar os valores atuais de consumo, mostrando tendências de crescimento, quedas abruptas, picos pontuais ou períodos de estabilidade. Dessa forma, o usuário consegue identificar rapidamente mudanças no padrão de operação que podem exigir investigação ou ajuste no planejamento.

A linha horizontal tracejada em vermelho indica a demanda prevista para o período, calculada com base na média móvel histórica. Quando a curva de consumo real se aproxima dessa linha, o sistema sinaliza um cenário de atenção. Caso o consumo ultrapasse a linha vermelha, caracteriza-se uma condição de alerta, indicando que a linha está operando acima do nível esperado, o que pode gerar risco de desequilíbrio no abastecimento ou pressão excessiva sobre os recursos disponíveis.

```sql

SELECT
    bucket_start AS time,
    (
        "5UK8" + "5UKN" + "5UKW" + "5URN" + "5URT" +
        "BZ42" + "BZ43" + "BZ44" + "BZ4A" +
        "CH21" + "CH22" + "CH23" + "CH24" + "CH29" +
        "R111"
    ) AS total
FROM public.bank_hourly_matrix
WHERE bucket_start >= now() - interval '30 days'
ORDER BY bucket_start;


```

Este código é utilizado para alimentar o gráfico de evolução do consumo total de bancos ao longo do tempo. Ele consulta a tabela `bank_hourly_matrix`, que armazena os dados de consumo agregados por intervalo horário, e prepara as informações no formato esperado pelo Grafana.

O campo `bucket_start` é selecionado como `time`, definindo o eixo temporal do gráfico. Em seguida, todas as colunas que representam os diferentes tipos de bancos são somadas, resultando no valor `total`, que corresponde ao consumo total de bancos em cada intervalo.

O filtro `bucket_start >= now() - interval '30 days'` limita a consulta aos últimos 30 dias, garantindo um histórico recente e relevante para análise visual, além de contribuir para melhor performance da consulta. Por fim, os resultados são ordenados cronologicamente, permitindo que o Grafana represente corretamente a evolução do consumo ao longo do tempo.

**Como é calculado:**

- A consulta utiliza a tabela `bank_hourly_matrix`, que contém os dados de consumo de bancos agregados por intervalo horário;
- O campo `bucket_start` é selecionado como referência temporal (`time`), sendo utilizado pelo Grafana para construir o eixo do tempo;
- Para cada registro, todas as colunas correspondentes aos diferentes tipos de bancos são somadas, resultando no valor `total`, que representa o consumo total no intervalo;
- Aplica-se um filtro temporal para considerar apenas os dados dos últimos 30 dias, garantindo relevância e desempenho;
- Os resultados são ordenados por `bucket_start`, assegurando a correta visualização da evolução do consumo ao longo do tempo.

**Sistema de Alerta** 

<div align="center">
<sub>Figura 6 - Alerta Banco</sub>
</div>
<div align="center">
<img src="../../assets/alerta_banco.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

Este gráfico possui um sistema de alerta integrado que é acionado quando o valor de consumo real ultrapassa o limite definido, representado visualmente pela linha de referência no gráfico.

Ao ser atingida essa condição, o sistema dispara automaticamente um alerta, sinalizando que a linha de produção está operando acima do nível esperado. Como ação imediata, é enviado um e-mail de notificação para os responsáveis, informando a ocorrência do desvio.

<div align="center">
<sub>Figura 7 - Email Alerta</sub>
</div>
<div align="center">
<img src="../../assets/email_alerta.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

#### 3.1.5 Consumo mensal de bancos na linha vs limite operacional 

<div align="center">
<sub>Figura 8 - Consumo Mensal de Bancos</sub>
</div>
<div align="center">
<img src="../../assets/consumo_mensal_bancos.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

Este gráfico compara o consumo mensal acumulado de bancos da linha de produção com limites operacionais previamente definidos. Cada barra representa o total consumido em um determinado dia, enquanto as linhas de referência indicam níveis aceitáveis e críticos de operação. A linha amarela indica o ponto em que o consumo atinge a previsão de demanda, servindo como um limite de referência para operação dentro do planejamento esperado. Já a linha vermelha representa a capacidade máxima da linha, sinalizando o limite operacional superior.Quando o consumo permanece abaixo da linha amarela, a operação está confortável. Ao se aproximar ou ultrapassar a linha amarela, o gráfico indica um cenário de atenção. Caso o consumo ultrapasse a linha vermelha, caracteriza-se uma condição crítica, indicando que a linha está operando acima da sua capacidade máxima, o que pode gerar riscos operacionais e logísticos.

Essa visualização é essencial para o acompanhamento do consumo acumulado e para apoiar decisões de planejamento, permitindo antecipar ajustes e evitar situações de excesso ou falta de bancos na linha de produção.

**Código SQL utilizado:**

```sql

WITH consumo_diario AS (
    SELECT 
        DATE(bucket_start) AS day,
        SUM(
            "5UK8" + "5UKN" + "5UKW" + "5URN" + "5URT" +
            "BZ42" + "BZ43" + "BZ44" + "BZ4A" +
            "CH21" + "CH22" + "CH23" + "CH24" +
            "CH29" + "R111"
        ) AS total_bancos_dia
    FROM public.bank_hourly_matrix
    WHERE bucket_start >= date_trunc('day', now()) - interval '30 days'
      AND bucket_start <  date_trunc('day', now()) + interval '1 day'
    GROUP BY 1
)

SELECT
    day,
    total_bancos_dia
FROM consumo_diario
WHERE total_bancos_dia > 0
ORDER BY day;


```

#### 3.2 Monitoramento da demanda de bancos divida por tipos 

<div align="center">
<sub>Figura 9 - Monitoramento da demanda de bancos divida por tipos</sub>
</div>
<div align="center">
<img src="../../assets/monitoramento_dividido.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

Esta seção do dashboard apresenta a demanda de bancos segmentada por tipo, permitindo uma análise mais detalhada do consumo na linha de produção. Diferentemente da visão geral, aqui o foco está em entender quais tipos de bancos estão sendo mais utilizados, em quais volumes e como esse comportamento evolui ao longo do tempo. Os indicadores e gráficos desta seção possibilitam identificar rapidamente os tipos de bancos com maior demanda atual, comparar volumes consumidos entre diferentes códigos e acompanhar a evolução individual de cada tipo. Essa segmentação é fundamental para apoiar decisões de abastecimento, priorização logística e ajustes no planejamento, especialmente em cenários onde determinados tipos apresentam consumo acima do padrão.

#### 3.2.1 Demanda atual da linha por tipo de banco 

<div align="center">
<sub>Figura 10 - Demanda atual da linha por tipo de banco</sub>
</div>
<div align="center">
<img src="../../assets/demanda_dividido.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

Este gráfico de barras apresenta a demanda atual da linha de produção segmentada por tipo de banco. Cada barra representa o volume consumido de um código específico, permitindo identificar rapidamente quais tipos estão com maior ou menor demanda no momento atual. 

**Código SQL utilizado:**

```sql

SELECT
  DATE(bucket_start) AS day,

  SUM("5UK8") AS "5UK8",
  SUM("5UKN") AS "5UKN",
  SUM("5UKW") AS "5UKW",
  SUM("5URN") AS "5URN",
  SUM("5URT") AS "5URT",

  SUM("BZ42") AS "BZ42",
  SUM("BZ43") AS "BZ43",
  SUM("BZ44") AS "BZ44",
  SUM("BZ4A") AS "BZ4A",

  SUM("CH21") AS "CH21",
  SUM("CH22") AS "CH22",
  SUM("CH23") AS "CH23",
  SUM("CH24") AS "CH24",
  SUM("CH29") AS "CH29",

  SUM("R111") AS "R111"

FROM bank_hourly_matrix
GROUP BY day
ORDER BY day;


```

#### 3.2.2 Rancking e tabela dos tipos de bancos mais consumidos nos últimos 14 dias 

<div align="center">
<sub>Figura 11 - Rancking e tabela dos tipos de bancos mais consumidos nos últimos 14 dias</sub>
</div>
<div align="center">
<img src="../../assets/rancking_tipos.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

Este gráfico de barras ordenadas apresenta um rancking dos tipos de bancos mais consumidos na linha de produção nos últimos 14 dias. Cada barra representa o volume total consumido de um código específico durante esse período, permitindo identificar rapidamente quais tipos estão com maior demanda acumulada. A tabela ao lado complementa a visualização, detalhando os valores exatos de consumo para cada tipo de banco.

**Código SQL utilizado:**

```sql

SELECT
  tipo_banco,
  total_consumido
FROM (
  SELECT '5UK8' AS tipo_banco, SUM("5UK8") AS total_consumido
  FROM public.bank_hourly_matrix
  WHERE bucket_start >= date_trunc('day', now()) - interval '14 days'
    AND bucket_start <  date_trunc('day', now())

  UNION ALL
  SELECT '5UKN', SUM("5UKN")
  FROM public.bank_hourly_matrix
  WHERE bucket_start >= date_trunc('day', now()) - interval '14 days'
    AND bucket_start <  date_trunc('day', now())

  UNION ALL
  SELECT '5UKW', SUM("5UKW")
  FROM public.bank_hourly_matrix
  WHERE bucket_start >= date_trunc('day', now()) - interval '14 days'
    AND bucket_start <  date_trunc('day', now())

# Continua para todos os tipos de bancos...

) t
WHERE total_consumido > 0
ORDER BY total_consumido DESC;

```
A lógica consiste em somar, individualmente, cada coluna correspondente a um tipo de banco dentro da tabela `bank_hourly_matrix`, sempre aplicando o mesmo recorte temporal (últimos 14 dias, excluindo o dia atual). Cada soma é transformada em uma linha identificada pelo respectivo `tipo_banco` por meio do uso de `UNION ALL`.


#### 3.2.3 Evolução na demanda de cada tipo de banco 

<div align="center">
<sub>Figura 12 - Evolução na demanda de cada tipo de banco </sub>
</div>
<div align="center">
<img src="../../assets/evolucao_demanda_total.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

Este gráfico apresenta a evolução temporal da demanda para cada tipo de banco utilizado na linha de produção. Cada linha representa um código de banco distinto, permitindo acompanhar individualmente como o consumo de cada tipo varia ao longo dos dias. A principal utilidade dessa visualização é possibilitar a comparação entre os diferentes tipos, evidenciando quais apresentam maior volume, maior volatilidade ou picos pontuais de consumo. Dessa forma, torna-se mais fácil identificar comportamentos atípicos ou mudanças no padrão de demanda que poderiam passar despercebidas em análises agregadas.

A visualização é interativa: ao clicar no código do tipo de banco desejado na legenda, o usuário pode habilitar ou desabilitar a exibição das curvas, permitindo visualizar um único tipo de forma isolada ou comparar apenas os tipos de interesse.

**Código SQL utilizado:**

```sql 
SELECT
    bucket_start AS hora,

    -- LINHA 5U
    "5UK8" AS "5UK8",
    "5UKN" AS "5UKN",
    "5UKW" AS "5UKW",
    "5URN" AS "5URN",
    "5URT" AS "5URT",

    -- BZ
    "BZ42" AS "BZ42",
    "BZ43" AS "BZ43",
    "BZ44" AS "BZ44",
    "BZ4A" AS "BZ4A",

    -- CH
    "CH21" AS "CH21",
    "CH22" AS "CH22",
    "CH23" AS "CH23",
    "CH24" AS "CH24",
    "CH29" AS "H29",

    -- R
    "R111" AS "R111"

FROM bank_hourly_matrix
ORDER BY hora;

```
Essa consulta seleciona o campo `bucket_start` como `hora`, que representa o intervalo de tempo para cada registro, e todas as colunas correspondentes aos diferentes tipos de bancos, mantendo seus nomes originais para facilitar a identificação no gráfico. Os resultados são ordenados cronologicamente por `hora`, permitindo que o Grafana represente corretamente a evolução do consumo ao longo do tempo.

#### 3.3 Monitoramento da demanda do banco selecionado 

Um dos features do dashboard é a possibilidade de filtrar todos os gráficos e indicadores para um tipo específico de banco ou roda. Isso é feito por meio de um filtro interativo localizado na parte superior do painel, onde o usuário pode selecionar o código do banco desejado. Ao fazer essa seleção, todos os componentes do dashboard são atualizados automaticamente para refletir apenas os dados relacionados ao banco escolhido.

Essa funcionalidade é especialmente útil para análises detalhadas, permitindo que o usuário foque em um tipo específico de peça e avalie seu comportamento ao longo do tempo, sua demanda atual, evolução e comparação com a previsão. Dessa forma, é possível identificar rapidamente quaisquer desvios ou padrões específicos que possam exigir atenção ou ajustes no planejamento.

<div align="center">
<sub>Figura 13 - Monitoramento da demanda do banco selecionado </sub>
</div>
<div align="center">
<img src="../../assets/analise_demanda_banco_selecionado.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

#### 3.3.1 Demanda atual do banco selecionado na linha de produção

<div align="center">
<sub>Figura 14 - Demanda atual do banco selecionado na linha de produção </sub>
</div>
<div align="center">
<img src="../../assets/demanda_tipo.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

**SQL utilizado:**

```sql  

WITH diario AS (
  SELECT
    DATE(bucket_start) AS dia,
    SUM(
      CASE '$Tipo_Banco'
        WHEN '5UK8' THEN "5UK8"
        WHEN '5UKN' THEN "5UKN"
        WHEN '5UKW' THEN "5UKW"
        WHEN '5URN' THEN "5URN"
        WHEN '5URT' THEN "5URT"
        WHEN 'BZ42' THEN "BZ42"
        WHEN 'BZ43' THEN "BZ43"
        WHEN 'BZ44' THEN "BZ44"
        WHEN 'BZ4A' THEN "BZ4A"
        WHEN 'CH21' THEN "CH21"
        WHEN 'CH22' THEN "CH22"
        WHEN 'CH23' THEN "CH23"
        WHEN 'CH24' THEN "CH24"
        WHEN 'CH29' THEN "CH29"
        WHEN 'R111' THEN "R111"
        ELSE 0
      END
    ) AS total_dia
  FROM public.bank_hourly_matrix
  GROUP BY dia
)

SELECT
  dia,
  total_dia
FROM diario
WHERE dia >= CURRENT_DATE - INTERVAL '7 days'
ORDER BY dia;

```
A lógica do código funciona da seguinte forma:


- Dentro da agregação, é utilizado um bloco `CASE` associado à variável `$Tipo_Banco`, que representa um parâmetro do Grafana;
- Esse `CASE` seleciona apenas a coluna correspondente ao tipo de banco escolhido pelo usuário no dashboard, retornando o valor daquela coluna e zero para todas as demais;
- A soma (`SUM`) garante que apenas o consumo do tipo selecionado seja consolidado no total diário (`total_dia`);
- Após a agregação, a consulta principal filtra os últimos 7 dias, limitando a visualização a um período recente e relevante;
- Os resultados são ordenados cronologicamente para permitir a correta visualização da evolução diária do consumo no gráfico.

#### 3.3.2 Previsão de demanda diária do banco selecionado

Assim como no indicador geral, este painel apresenta a previsão de demanda diária, mas focada exclusivamente no banco selecionado pelo usuário. A previsão é calculada com base na média móvel dos últimos 14 dias completos, excluindo o dia atual para evitar distorções por dados parciais.

<div align="center">
<sub>Figura 15 - Previsão de demanda diária do banco selecionado </sub>
</div>
<div align="center">
<img src="../../assets/previsao_tipo.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

**SQL utilizado:**

```sql

WITH consumo_diario AS (
  SELECT
    date_trunc('day', bucket_start) AS dia,
    SUM(
      CASE '$Tipo_Banco'
        WHEN '5UK8' THEN "5UK8"
        WHEN '5UKN' THEN "5UKN"
        WHEN '5UKW' THEN "5UKW"
        WHEN '5URN' THEN "5URN"
        WHEN '5URT' THEN "5URT"
        WHEN 'BZ42' THEN "BZ42"
        WHEN 'BZ43' THEN "BZ43"
        WHEN 'BZ44' THEN "BZ44"
        WHEN 'BZ4A' THEN "BZ4A"
        WHEN 'CH21' THEN "CH21"
        WHEN 'CH22' THEN "CH22"
        WHEN 'CH23' THEN "CH23"
        WHEN 'CH24' THEN "CH24"
        WHEN 'CH29' THEN "CH29"
        WHEN 'R111' THEN "R111"
        ELSE 0
      END
    ) AS consumido_dia
  FROM public.bank_hourly_matrix
  WHERE bucket_start >= date_trunc('day', now()) - interval '15 days'
    AND bucket_start <  date_trunc('day', now())          -- exclui hoje
  GROUP BY 1
),

ultimos_14_dias AS (
  SELECT
    consumido_dia
  FROM consumo_diario
  WHERE dia >= date_trunc('day', now()) - interval '14 days'
    AND dia <  date_trunc('day', now())                  -- garante até ontem
    AND consumido_dia > 0                                -- remove dias com zero (igual seu 1º)
)

SELECT
  ROUND(AVG(consumido_dia)::numeric, 2) AS previsao_diaria_mm_14d
FROM ultimos_14_dias;

```

#### 3.3.3 Relação demanda real vs prevista (%) do banco selecionado

Assim como no indicador geral, este painel apresenta a relação percentual entre a demanda real e a prevista, mas focada exclusivamente no banco selecionado pelo usuário. O indicador é construído a partir da razão entre o consumo real observado no dia e o valor de previsão diária, sendo expresso em percentual.

<div align="center">
<sub>Figura 16 - Relação demanda real vs prevista (%) do banco selecionado </sub>
</div>
<div align="center">
<img src="../../assets/relacao_tipo.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

**SQL utilizado:**

```sql

WITH consumo_diario AS (
  SELECT
    date_trunc('day', bucket_start)::date AS dia,
    SUM(
      CASE '$Tipo_Banco'
        WHEN '5UK8' THEN "5UK8"
        WHEN '5UKN' THEN "5UKN"
        WHEN '5UKW' THEN "5UKW"
        WHEN '5URN' THEN "5URN"
        WHEN '5URT' THEN "5URT"
        WHEN 'BZ42' THEN "BZ42"
        WHEN 'BZ43' THEN "BZ43"
        WHEN 'BZ44' THEN "BZ44"
        WHEN 'BZ4A' THEN "BZ4A"
        WHEN 'CH21' THEN "CH21"
        WHEN 'CH22' THEN "CH22"
        WHEN 'CH23' THEN "CH23"
        WHEN 'CH24' THEN "CH24"
        WHEN 'CH29' THEN "CH29"
        WHEN 'R111' THEN "R111"
        ELSE 0
      END
    )::numeric AS consumo_dia
  FROM public.bank_hourly_matrix
  GROUP BY 1
),

-- média móvel dos últimos 14 dias completos (exclui HOJE e dias zero)
mm_14d AS (
  SELECT
    AVG(consumo_dia) AS media_movel_14d
  FROM (
    SELECT consumo_dia
    FROM consumo_diario
    WHERE
      dia < date_trunc('day', now())::date  -- exclui HOJE
      AND consumo_dia > 0                  -- exclui dias zero
    ORDER BY dia DESC
    LIMIT 14
  ) t
),

-- consumo do dia de HOJE (parcial, até agora)
consumo_hoje AS (
  SELECT
    COALESCE(consumo_dia, 0) AS consumo_hoje
  FROM consumo_diario
  WHERE dia = date_trunc('day', now())::date
)

SELECT
  ROUND(
    (consumo_hoje.consumo_hoje / NULLIF(mm_14d.media_movel_14d, 0)) * 100
  , 2) AS pct_consumo_hoje_vs_mm_14d
FROM consumo_hoje
CROSS JOIN mm_14d;

```

#### 3.3.4 Evolução na demanda do banco selecionado ao longo do tempo

<div align="center">
<sub>Figura 17 - Evolução na demanda do banco selecionado ao longo do tempo </sub>
</div>
<div align="center">
<img src="../../assets/evolucao_tipo_banco.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

**SQL utilizado:**

```sql

SELECT
    bucket_start AS time,

    CASE
        WHEN '$Tipo_Banco' = '5UK8' THEN "5UK8"
        WHEN '$Tipo_Banco' = '5UKN' THEN "5UKN"
        WHEN '$Tipo_Banco' = '5UKW' THEN "5UKW"
        WHEN '$Tipo_Banco' = '5URN' THEN "5URN"
        WHEN '$Tipo_Banco' = '5URT' THEN "5URT"

        WHEN '$Tipo_Banco' = 'BZ42' THEN "BZ42"
        WHEN '$Tipo_Banco' = 'BZ43' THEN "BZ43"
        WHEN '$Tipo_Banco' = 'BZ44' THEN "BZ44"
        WHEN '$Tipo_Banco' = 'BZ4A' THEN "BZ4A"

        WHEN '$Tipo_Banco' = 'CH21' THEN "CH21"
        WHEN '$Tipo_Banco' = 'CH22' THEN "CH22"
        WHEN '$Tipo_Banco' = 'CH23' THEN "CH23"
        WHEN '$Tipo_Banco' = 'CH24' THEN "CH24"
        WHEN '$Tipo_Banco' = 'CH29' THEN "CH29"

        WHEN '$Tipo_Banco' = 'R111' THEN "R111"

        ELSE 0
    END AS total

FROM bank_hourly_matrix
ORDER BY bucket_start;

```

#### 3.3.5 Consumo mensal do banco selecionado vs limite operacional

<div align="center">
<sub>Figura 18 - Consumo mensal do banco selecionado vs limite operacional </sub>
</div>
<div align="center">
<img src="../../assets/consumo_mensal_tipo.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

**SQL utilizado:**

```sql

SELECT 
  DATE(bucket_start) AS day,
  SUM(
    CASE 
      WHEN '$Tipo_Banco' = '5UK8' THEN "5UK8"
      WHEN '$Tipo_Banco' = '5UKN' THEN "5UKN"
      WHEN '$Tipo_Banco' = '5UKW' THEN "5UKW"
      WHEN '$Tipo_Banco' = '5URN' THEN "5URN"
      WHEN '$Tipo_Banco' = '5URT' THEN "5URT"
      WHEN '$Tipo_Banco' = 'BZ42' THEN "BZ42"
      WHEN '$Tipo_Banco' = 'BZ43' THEN "BZ43"
      WHEN '$Tipo_Banco' = 'BZ44' THEN "BZ44"
      WHEN '$Tipo_Banco' = 'BZ4A' THEN "BZ4A"
      WHEN '$Tipo_Banco' = 'CH21' THEN "CH21"
      WHEN '$Tipo_Banco' = 'CH22' THEN "CH22"
      WHEN '$Tipo_Banco' = 'CH23' THEN "CH23"
      WHEN '$Tipo_Banco' = 'CH24' THEN "CH24"
      WHEN '$Tipo_Banco' = 'CH29' THEN "CH29"
      WHEN '$Tipo_Banco' = 'R111' THEN "R111"
      ELSE 0
    END
  ) AS consumo_banco
FROM bank_hourly_matrix
GROUP BY day
ORDER BY day;

```

#### 3.4 Filtros globais do Dashboard

Na parte superior do dashboard, há dois filtros globais que permitem ao usuário ajustar a visualização dos dados. O primeiro filtro é o seletor de tipo de banco e roda, onde o usuário pode escolher um código específico para analisar. Ao selecionar um tipo, todos os gráficos e indicadores do dashboard são atualizados automaticamente para refletir apenas os dados relacionados ao banco e roda escolhido. O segundo filtro é o seletor de intervalo de datas, que permite ao usuário definir o período de interesse para a análise. Com esse filtro, é possível ajustar o escopo temporal dos dados exibidos, facilitando a comparação entre diferentes períodos ou a visualização de tendências ao longo do tempo. Vale ressaltar que alguns gráficos possuem intervalos fixos definidos em suas consultas SQL, não sendo afetados por esse filtro de data.

#### 3.5 Configuração de Alertas no Dashboard

<div align="center">
<sub>Figura 19 - Configuração de Alertas no Dashboard </sub>
</div>
<div align="center">
<img src="../../assets/alertas_bancos.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

O dashboard foi projetado para permitir a configuração de alertas de forma simples e flexível, possibilitando que o monitoramento da linha de produção seja adaptado às necessidades operacionais de cada cenário.

Atualmente, foram implementados dois alertas principais: um para identificar consumo de rodas acima da previsão e outro para identificar consumo de bancos acima da previsão. Em ambos os casos, a lógica do alerta utiliza como referência a previsão de demanda calculada a partir do histórico, permitindo detectar rapidamente desvios em relação ao comportamento esperado da operação.

Os valores de limite desses alertas são totalmente configuráveis. Embora o padrão adotado tenha sido a comparação com a previsão de demanda, esses limiares podem ser ajustados para outros critérios, como limites fixos, percentuais personalizados ou metas definidas pelo planejamento, conforme a necessidade do usuário.

Além disso, o canal de comunicação dos alertas também é flexível. No cenário atual, as notificações foram configuradas para envio por e-mail, garantindo que os responsáveis sejam informados imediatamente quando uma condição de alerta é atingida. No entanto, o sistema permite a utilização de outros canais de comunicação, como integrações com ferramentas de mensagens, sistemas externos ou webhooks, ampliando as possibilidades de automação e resposta rápida a eventos críticos.

#### 3.6 Dashboard para monitoramento de rodas

Para o monitoramento do consumo de rodas, foi utilizada exatamente a mesma lógica de visualização, estrutura de dashboard e raciocínio analítico aplicados aos bancos. Isso inclui os mesmos tipos de gráficos, indicadores de demanda atual, previsão por média móvel, relação percentual entre consumo real e previsto, além dos alertas configurados.

A única diferença está nos códigos dos componentes monitorados. Enquanto a seção de bancos trabalha com os códigos específicos de bancos, a seção de rodas utiliza os códigos correspondentes aos tipos de rodas produzidos e consumidos na linha.

Os códigos de rodas considerados nas consultas SQL são:

- `40I`
- `41P`
- `44M`
- `45H`
- `48E`
- `C0A`
- `C0V`
- `C1Y`
- `C4W`
- `C5N`
- `C6E`
- `CI1`
- `CI4`
- `CR4`
- `CV2`
- `V41`

Toda a lógica de cálculo permanece a mesma: os dados são agregados a partir da tabela horária, consolidados por período (dia ou hora), utilizados para cálculo de médias móveis e comparados com valores de referência para gerar indicadores visuais e alertas. 

Essa padronização garante consistência entre as análises de bancos e rodas, facilita a manutenção do dashboard e permite que o usuário interprete ambas as seções de forma intuitiva, sem a necessidade de aprender novas regras ou modelos de leitura.

## 4. Conclusão

Nesta seção, detalhamos o processo de verificação do funcionamento do sistema de monitoramento, bem como a estrutura e funcionalidades do dashboard desenvolvido para acompanhar o consumo de bancos e rodas na linha de produção. Foram apresentados os principais indicadores, gráficos e alertas configurados, além da lógica por trás dos cálculos utilizados para gerar essas visualizações. O dashboard foi projetado para oferecer uma visão clara e intuitiva do desempenho operacional, permitindo que os usuários tomem decisões informadas com base em dados atualizados e relevantes. A flexibilidade na configuração de alertas e a possibilidade de filtrar por tipos específicos de bancos e rodas tornam o sistema adaptável às necessidades variadas da operação.

---

**Elaborado por**: Time Sem Parar  
**Data**: Dezembro de 2025  
**Versão**: 1.0

---

