# Documentação Final do Projeto
## Solução de Internet das Coisas para Automação Sustentável - Monitoramento de Consumo de Rodas e Bancos

**Time Sem Parar**  
**Módulo: Administração Tech - IN04**  
**Parceiro: Volkswagen do Brasil**  
**Data:** Dezembro de 2025

---

## Sumário

1. [Introdução](#1-introdução)
2. [Definição do Problema e Objetivos](#2-definição-do-problema-e-objetivos)
3. [Fundamentação Técnica e Teórica](#3-fundamentação-técnica-e-teórica)
4. [Descrição da Solução e Decisões de Projeto](#4-descrição-da-solução-e-decisões-de-projeto)
5. [Dashboard de Monitoramento](#5-dashboard-de-monitoramento)
6. [Testes, Validações e Resultados](#6-testes-validações-e-resultados)
7. [Análise de Impacto e Viabilidade](#7-análise-de-impacto-e-viabilidade)
8. [Instruções de Uso e Implantação](#8-instruções-de-uso-e-implantação)
9. [Limitações, Riscos e Considerações Finais](#9-limitações-riscos-e-considerações-finais)
10. [Possibilidades de Evolução Futura](#10-possibilidades-de-evolução-futura)
11. [Referências](#11-referências)

---

## 1. Introdução

Este documento apresenta a documentação final do projeto de desenvolvimento de uma solução de Internet das Coisas (IoT) para automação sustentável na linha de montagem da Volkswagen do Brasil. O projeto foi desenvolvido ao longo de cinco sprints, com foco na rastreabilidade e monitoramento de consumo de componentes críticos da produção: rodas e bancos.

A solução desenvolvida integra tecnologias de Indústria 4.0 para criar um sistema de observabilidade em tempo real, permitindo o monitoramento preciso do consumo de peças, otimização de estoques e prevenção de paradas na linha de produção. O projeto contempla desde a concepção da arquitetura IoT até a validação através de testes de usabilidade, passando por análises de viabilidade econômica e otimização da cadeia de suprimentos.

O desenvolvimento seguiu uma metodologia ágil, com entregas incrementais que permitiram a validação contínua das decisões técnicas e de negócio, sempre alinhadas às necessidades operacionais da Volkswagen e aos princípios de produção Just-in-Time (JIT) e Just-in-Sequence (JIS).

---

## 2. Definição do Problema e Objetivos

### 2.1 Contexto e Problema Identificado

A linha de montagem da Volkswagen do Brasil opera em um ambiente de alta criticidade, onde cada minuto de parada pode gerar perdas estimadas em R$ 120.000,00 (Referência 11). O controle de estoque de componentes críticos, especialmente rodas e bancos, é fundamental para manter a continuidade da produção, que segue os princípios de Just-in-Time e Just-in-Sequence.

O problema central identificado foi a **falta de observabilidade unificada** sobre o consumo de peças em tempo real. A operação atual depende de:

- Processos manuais e intuição do operador para controle de estoque
- Uso limitado do SAP para monitoramento
- Recursos de inspeção por câmera que não cobrem 100% dos itens
- Decisões operacionais reativas, baseadas em relatórios defasados
- Alto risco de paralisação da linha por falta de componentes
- Retrabalho causado pela necessidade de substituição de peças reserva temporárias

Essa situação gera vulnerabilidades operacionais significativas, onde a descoberta tardia de baixos níveis de estoque pode resultar em paradas não programadas, impactando diretamente a produtividade e os custos operacionais.

### 2.2 Objetivos do Projeto

#### 2.2.1 Objetivo Geral

Desenvolver uma solução de IoT para monitoramento e controle de consumo de rodas e bancos na linha de montagem da Volkswagen, proporcionando visibilidade em tempo real, otimização de estoques e prevenção de paradas não programadas.

#### 2.2.2 Objetivos Específicos

1. **Observabilidade em Tempo Real**
   - Implementar um dashboard centralizado que apresente dados de consumo atualizados com latência inferior a 5 minutos
   - Criar sistema de alertas proativos (Verde/Amarelo/Vermelho) baseado em níveis de estoque e comportamento histórico

2. **Otimização de Estoques**
   - Desenvolver modelo de otimização da cadeia de suprimentos que minimize estoques mantendo segurança operacional
   - Implementar previsão de consumo baseada em histórico para manutenção de estoque mínimo seguro

3. **Rastreabilidade e Qualidade**
   - Garantir rastreabilidade unívoca de componentes (rodas e bancos) associados ao número de chassi (VIN)
   - Integrar dados de qualidade (torque, posicionamento) com sistemas corporativos

4. **Redução de Riscos Operacionais**
   - Reduzir em 95% o risco de paradas não programadas por falta de peças
   - Eliminar dependência de processos manuais e intuição para controle de estoque
   - Reduzir retrabalho causado pelo uso de peças reserva temporárias, garantindo disponibilidade da peça correta no momento da montagem

5. **Viabilidade Econômica**
   - Demonstrar viabilidade financeira através de análise de ROI, VPL e TIR
   - Justificar investimento através de redução de custos operacionais e prevenção de perdas

### 2.3 Relevância e Alinhamento

Os objetivos propostos estão diretamente alinhados com:

- **Estratégia de Indústria 4.0 da Volkswagen**: Digitalização e automação de processos produtivos
- **Princípios JIT/JIS**: Otimização de estoques e sincronização de abastecimento
- **Redução de Custos Operacionais**: Prevenção de paradas e otimização de recursos
- **Melhoria Contínua**: Base de dados para análise e tomada de decisão estratégica

---

## 3. Fundamentação Técnica e Teórica

### 3.1 Fundamentação em Indústria 4.0

A Indústria 4.0 representa a quarta revolução industrial, caracterizada pela integração entre automação, Internet das Coisas industrial (IoT), sistemas ciberfísicos, análise de dados em tempo real e tomadas de decisão suportadas por algoritmos (Referência 3). A aplicação desses elementos transforma fluxos produtivos tradicionais em processos conectados e observáveis.

#### 3.1.1 Pilares Aplicados ao Projeto

O projeto fundamenta-se em três pilares principais da Indústria 4.0:

1. **Automação**: Execução de tarefas padronizadas por sistemas/atuadores com menor intervenção humana (Referência 5). No contexto do projeto, a automação se manifesta através de sensores que coletam dados automaticamente e sistemas que processam informações sem intervenção manual.

2. **IoT (Internet das Coisas)**: Sensores e leitores que coletam dados de processo em tempo real para alimentar pipelines e dashboards (Referência 3). O projeto utiliza leitores UHF SICK, sensores de torque HBM, sensores de posicionamento Balluff e sensores de vibração IFM para coleta contínua de dados.

3. **Integração Ciberfísica**: Conexão entre equipamentos físicos (leitores Keyence e SICK) e sistemas digitais (Node-RED, pipeline, dashboard), permitindo visibilidade e ações baseadas em dados (Referência 11). A arquitetura desenvolvida integra camadas de percepção (OT) com camadas de aplicação (TI).

### 3.2 Fundamentação em Otimização de Supply Chain

A otimização da cadeia de suprimentos é fundamental para operações Just-in-Time. O projeto aplica conceitos de **Programação Linear** para minimizar estoques mantendo segurança operacional.

#### 3.2.1 Modelo de Otimização

O modelo desenvolvido utiliza programação linear com a biblioteca PuLP em Python, seguindo a formulação:

**Função Objetivo:**
```
Minimizar: x1 + x2 + x3
```

**Restrições:**
- Capacidade máxima de estoque: `(x1 + x2 + x3) ≤ E_max` (onde E_max = 4.096 rodas)
- Demanda mínima por tipo: `xi ≥ xi_min` (para i = 1, 2, 3)
- Demanda máxima por tipo: `xi ≤ xi_max` (para i = 1, 2, 3)

Onde:
- `x1, x2, x3` representam quantidades de rodas dos tipos 41P, C0V e CR4, respectivamente
- `E_max` é a capacidade total do estoque (4.096 rodas, calculada como 21.846 rodas totais ÷ 16 modelos × 3 modelos analisados)
- `xi_min` são demandas mínimas calculadas a partir da semana anterior ao período de análise
- `xi_max` são demandas máximas: x1_max = 136 rodas (tipo 41P), x2_max = 128 rodas (tipo C0V), x3_max = 168 rodas (tipo CR4)

Este modelo garante que o estoque seja mantido no nível mínimo necessário para atender à demanda, alinhado aos princípios JIT/JIS.

### 3.3 Fundamentação em Arquitetura IoT

A arquitetura IoT desenvolvida segue o modelo de três camadas amplamente adotado na indústria:

1. **Camada de Percepção (Perception Layer)**: Sensores e atuadores no chão de fábrica
2. **Camada de Comunicação (Communication Layer)**: Protocolos e gateways para transmissão de dados
3. **Camada de Aplicação (Application Layer)**: Processamento, armazenamento e visualização

#### 3.3.1 Protocolos Industriais

O projeto utiliza protocolos padrão da indústria:

- **OPC-UA (OPC Unified Architecture)**: Comunicação industrial padronizada entre CLPs Siemens S7-1500/1200 e gateways, garantindo interoperabilidade e segurança (Referência 8)
- **MQTT (Message Queuing Telemetry Transport)**: Protocolo leve e assíncrono para comunicação entre gateways e middleware, ideal para telemetria IoT
- **REST API**: Integração com sistemas legados (FIS/CobrA) para troca de dados bidirecional

### 3.4 Benchmarking e Melhores Práticas

O projeto foi fundamentado em benchmarking com empresas líderes globais:

- **Hyundai Motor Company**: Referência em implementação de IoT e JIT em larga escala, com capacidade de 1,6 milhão de veículos/ano
- **Amazon**: Líder em gestão de estoque baseada em IoT, com acurácia superior a 99%
- **BYD**: Exemplo de integração vertical e uso de Big Data + IA para orquestração de recursos

As melhores práticas identificadas foram adaptadas ao contexto da Volkswagen, considerando restrições operacionais, padrões técnicos corporativos e viabilidade de implementação.

### 3.5 Referências Teóricas

A fundamentação teórica do projeto baseia-se em:

- **Kalsoom et al. (2021)** (Referência 3): Impacto do IoT na Indústria 4.0 e transformação de processos produtivos
- **Alshahrani (2023)** (Referência 1): Desafios e estratégias de mitigação na adoção de Indústria 4.0
- **Alsaadi (2022)** (Referência 2): Modelagem e análise de desafios de adoção da Indústria 4.0
- **OSTERWALDER (2014)** (Referência 4): Value Proposition Design para alinhamento de solução com necessidades do cliente

---

## 4. Descrição da Solução e Decisões de Projeto

### 4.1 Visão Geral da Solução

A solução desenvolvida é um **Painel de Observabilidade de IoT (MVP)** para o gerenciamento de consumo e estoque de peças críticas (rodas e bancos) na linha de montagem da Volkswagen. A solução integra:

- **Arquitetura IoT completa** (camadas de Perception, Communication e Application)
- **Dashboard interativo** para visualização e análise de dados em tempo real
- **Sistema de alertas proativos** baseado em níveis de estoque e comportamento histórico
- **Modelo de otimização** da cadeia de suprimentos
- **Pipeline de dados** em tempo real desenvolvido com tecnologias da Indústria 4.0

### 4.2 Componentes Principais

#### 4.2.1 Camada de Percepção e Controle (OT - Chão de Fábrica)

A base da arquitetura no chão de fábrica é composta por:

**Sensores de Identificação:**
- **Leitores UHF SICK RFU620**: 4 unidades localizadas em pontos críticos (M100, Tacto 123, Tacto 127, G700) para rastreabilidade de componentes (Referência 9)

**Sensores de Medição:**
- **Sensores de Torque HBM T10F**: 4 unidades por ponto de montagem de rodas (Tacto 123), garantindo precisão de laboratório no controle de qualidade (Referência 10)
- **Sensores de Posicionamento Balluff BTL**: 4 unidades por ponto para verificação de posicionamento correto das rodas
- **Sensores de Vibração IFM/VSA**: 1 unidade por motor/equipamento crítico para monitoramento preditivo

**Atuadores:**
- **Chaves de Aperto Eletrônicas Atlas Copco Tensor DS**: 4 atuadores para montagem de rodas com controle preciso de torque

**Controladores:**
- **PLCs Siemens S7-1500**: 3 unidades para pontos críticos (Tacto 123, Supervisão, Redundância) com alta capacidade de processamento (32-44 pontos de I/O para conexão de sensores e atuadores) (Referência 8)
- **PLCs Siemens S7-1200**: 3 unidades para pontos secundários (M100, Tacto 127, G700) com média capacidade (16-22 pontos de I/O para conexão de sensores e atuadores) (Referência 8)

**Justificativa das Escolhas:**
- **Siemens como padrão inegociável**: Garante compatibilidade com ecossistema existente da Volkswagen, suporte técnico local e disponibilidade de técnicos certificados (Referência 8)
- **Redundância N+1**: Proteção contra custo de parada de R$ 120.000/min, garantindo disponibilidade de 99,99%
- **Sensores HBM de alta precisão**: Requisito de qualidade de laboratório para evitar recalls por falha de segurança (Referência 10)

#### 4.2.2 Camada de Comunicação (Conectividade e Protocolos)

A integração entre OT e TI é realizada através de:

**Rede Física:**
- **Cabo Rede Industrial TCP/IP Cabeado**: Conexão física para dados em tempo real de baixa latência, evitando interferências do ambiente fabril

**Infraestrutura de Rede:**
- **Switches Industriais Siemens Scalance**: Distribuição de rede e redundância em anel
- **Gateway OT/TI Siemens IOT2050**: Interface entre PLCs e servidores, garantindo segregação de rede

**Protocolos:**
- **OPC-UA**: Comunicação industrial padronizada nativa nos PLCs Siemens S7-1500/1200 (Referência 8)
- **MQTT**: Comunicação leve e assíncrona com middleware Node-RED para telemetria (Referência 7)

**Justificativa das Escolhas:**
- **Rede cabeada**: Garante estabilidade, baixa latência e consistência de taxa de transferência, vitais para controle em tempo real
- **Protocolos padrão da indústria**: OPC-UA e MQTT são amplamente adotados, garantindo interoperabilidade e suporte técnico

#### 4.2.3 Camada de Aplicação (TI - Servidor e Dados)

Esta camada processa mais de 50.000 eventos/hora:

**Infraestrutura de Servidores:**
- **Servidor IBM Power Master**: Ala 22 (primário) - Alta capacidade de processamento (Referência 6)
- **Servidor IBM Power Mirror**: Ala 13 (secundário) - Espelhamento síncrono para redundância (Referência 6)
- **PowerHA Cluster**: Failover automático com tempo de recuperação < 500ms (Referência 6)

**Banco de Dados:**
- **IBM DB2 Database**: Armazenamento transacional de missão crítica com SSD RAID-10, capacidade estimada de 6TB (Referência 6)

**Middleware e Orquestração:**
- **Node-RED**: Orquestração IoT e lógica de negócios, permitindo desenvolvimento rápido de flows para traduzir, processar e rotear dados entre protocolos díspares (Referência 7)

**Integração:**
- **APIs REST**: Integração com sistemas legados FIS/CobrA para troca de dados bidirecional

**Justificativa das Escolhas:**
- **IBM Power Systems**: Sistemas de missão crítica com alta disponibilidade, garantindo 99,99% de uptime (Referência 6)
- **Node-RED**: Ferramenta low-code e flexível, permitindo desenvolvimento rápido sem necessidade de reprogramação de CLPs (Referência 7)
- **DB2**: Banco de dados corporativo da IBM, alinhado com padrões da Volkswagen (Referência 6)

### 4.4 Modelo de Otimização de Supply Chain

O modelo de otimização desenvolvido utiliza programação linear para minimizar estoques mantendo segurança operacional. O modelo foi implementado em Python com a biblioteca PuLP e testado com dados reais de dois meses de produção.

**Resultados do Modelo:**
- Solução ótima encontrada respeitando todas as restrições (Status: Ótimo)
- Estoque mínimo calculado: 84 rodas total
  - 16 rodas tipo 41P (Virtus Alloy wheels 6J x 15)
  - 36 rodas tipo C0V (Virtus Steel wheels 7J x 15)
  - 32 rodas tipo CR4 (Saveiro Alloy wheels 6J x 15)
- Alinhamento com princípios JIT/JIS, mantendo estoque no nível mínimo necessário
- Valores respeitam todas as restrições: estoque total (84) ≤ capacidade máxima (4.096) e cada tipo dentro dos limites de demanda mínima e máxima

### 4.5 Decisões de Projeto

#### 4.5.1 Escolha de Tecnologias

**Siemens como Padrão:**
- Decisão baseada em padrão corporativo inegociável da Volkswagen
- Garante compatibilidade, suporte técnico local e disponibilidade de técnicos certificados (Referência 8)
- Reduz TCO (Total Cost of Ownership) através de padronização

**IBM Power Systems:**
- Decisão baseada em requisitos de alta disponibilidade (99,99%) (Referência 6)
- Capacidade de processamento para mais de 50.000 eventos/hora
- Suporte técnico 24/7 e histórico de confiabilidade em ambientes críticos

**Node-RED como Middleware:**
- Decisão baseada em flexibilidade e agilidade de desenvolvimento (Referência 7)
- Open Source elimina custo de licenciamento
- Permite mudanças de lógica de negócios sem reprogramação de CLPs

#### 4.5.2 Estratégia de Redundância

**Redundância N+1 em Múltiplas Camadas:**
- PLCs redundantes em configuração N+1 para pontos críticos
- Servidores em cluster PowerHA para alta disponibilidade
- Justificativa: Proteção contra custo de parada de R$ 120.000/min

#### 4.5.3 Estratégia de Integração

**APIs REST para Sistemas Legados:**
- Decisão de não integrar diretamente com SAP/MES no MVP
- Estratégia modular permite integração futura sem reescrever código
- Reduz complexidade inicial e permite validação incremental

### 4.6 Estrutura Técnica e Arquitetura

#### 4.6.1 Arquitetura Geral do Sistema

A arquitetura desenvolvida segue o modelo de três camadas, integrando Tecnologia Operacional (OT) e Tecnologia da Informação (TI):

<div align="center">
<sub>Figura 1 - Arquitetura IoT em Três Camadas</sub>
</div>
<div align="center">
<img src="../../assets/diagrama_simples_arquitetura.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

#### 4.6.2 Fluxo de Dados

O fluxo de dados segue a seguinte sequência:

1. **Coleta**: Sensores e leitores coletam dados no chão de fábrica (torque, posicionamento, identificação UHF)
2. **Consolidação**: CLPs Siemens consolidam dados dos sensores
3. **Transmissão**: Dados são transmitidos via OPC-UA para Gateway IOT2050
4. **Conversão**: Gateway converte protocolo OPC-UA para MQTT
5. **Orquestração**: Node-RED recebe dados via MQTT, aplica lógica de negócios e processa informações
6. **Armazenamento**: Dados são armazenados no DB2 para histórico e análise
7. **Visualização**: Dashboard consome dados em tempo real para apresentação aos usuários
8. **Integração**: APIs REST permitem integração com sistemas legados (FIS/CobrA)

#### 4.6.3 Diagrama de Arquitetura Detalhado

<div align="center">
<sub>Figura 2 - Arquitetura IoT Completa</sub>
</div>
<div align="center">
<img src="../../assets/Diagrama sem nome.drawio.svg">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

**Legenda do Diagrama:**
- **Protocolos e Direção de Fluxo:**
  - OPC-UA (seta azul): Comunicação PLC → Gateway (bidirecional)
  - MQTT (seta verde): Comunicação Gateway → Middleware (publish/subscribe)
  - REST (seta laranja): Comunicação Middleware → Sistemas Legados (request/response)
  - TCP/IP (linha preta): Rede física cabeada

- **Notas de Segurança:**
  - VLANs segregadas: OT (VLAN 100), TI (VLAN 200), DMZ (VLAN 300)
  - Firewall entre camadas OT e TI
  - Autenticação MQTT via certificados X.509

#### 4.6.4 Especificações Técnicas Detalhadas

##### 4.6.4.1 Capacidade e Performance

| Métrica | Especificação | Justificativa |
|---------|---------------|---------------|
| **Eventos/hora** | 50.000+ | Capacidade para processar todos os eventos da linha de montagem |
| **Latência (Sensor → BD)** | < 200ms (p95) | Tempo real suficiente para alertas proativos |
| **Tempo de Recuperação (Failover)** | < 500ms | Transparente para operação, sem impacto na produção |
| **Disponibilidade do Sistema** | 99,99% | 4,38 minutos de downtime/ano, aceitável para operação crítica |
| **Taxa de Erro de Dados** | < 0,1% | Garante confiabilidade das informações apresentadas |

##### 4.6.4.2 Segurança e Governança

- **Segregação de Rede**: VLANs separadas para OT, TI e DMZ
- **Autenticação**: Certificados X.509 para comunicação MQTT
- **Firewall**: Proteção entre camadas OT e TI
- **Logs de Auditoria**: Registro de todas as operações para rastreabilidade

#### 4.6.5 Lógica de Dimensionamento

##### 4.6.5.1 Sensores e Leitores

- **1 leitor UHF por ponto crítico de identificação**: M100, Tacto 123, Tacto 127, G700
- **4 sensores de torque por ponto de montagem**: 1 por posição de roda (4 rodas)
- **4 sensores de posicionamento por ponto**: 1 por posição de roda
- **1 sensor de vibração por equipamento crítico**: Monitoramento preditivo

##### 4.6.5.2 Controladores

- **PLCs S7-1500**: Alta capacidade (32-44 pontos) para pontos críticos
- **PLCs S7-1200**: Média capacidade (16-22 pontos) para pontos secundários
- **Redundância N+1**: PLC adicional para pontos críticos (Tacto 123)

##### 4.6.5.3 Infraestrutura de Rede

- **1 switch por célula + redundância**: Distribuição de rede e redundância em anel
- **1 gateway por grupo de 3-5 CLPs**: Interface PLC-Servidor
- **20-30% extra de cabo**: Folga para expansões futuras

---

## 5. Dashboard de Monitoramento

### 5.1. Introdução

Fazendo jus ao nome da equipe, o dashboard da *Sem Parar* foi projetado pensando em maneiras de facilitar o monitoramento do consumo de rodas e bancos na linha de produção, de modo a evitar quaisquer interrupções devido à falha no alinhamento entre o consumo real e o previsto. 
Sabendo que a agilidade na tomada de decisão é crucial para manter a eficiência operacional, o dashboard foi cuidadosamente arquitetado olhando para o usuário final, que são os gestores e operadores da linha de produção, que lidam com uma quntidade enorme de dados diariamenete e por isso, precisam de uma ferramenta que seja intuitiva a ponto de permitir que as informações relevantes sejam interpretadas em poucos segundos e sem muito esforço cognitivo. 
O dashboard permite tanto uma vizualização geral do consumo, quanto uma análise detalhada por tipo de peça, possibilitando identificar rapidamente quaisquer desvios entre o consumo real e o previsto, além de destacar áreas que necessitam de atenção imediata. Foram também configurados alertas para que o usuário não deixe passar despercebido quando os limites críticos forem atingidos. 

## 5.2. Instruções para uso do Dashboard

O dashboard se baseia em uma arquitetura orientada a eventos, representada pelo seguinte fluxo:

**Sensores / Eventos → Fila (RabbitMQ) → Python → PostgreSQL → Grafana**

Cada componente tem um papel específico:
- A fila garante resiliência e desacoplamento;
- O script Python processa e valida os dados;
- O banco de dados organiza as informações para consulta eficiente;
- O Grafana consome os dados já tratados e agregados.

#### 5.2.1 Conexão com a Fila (RabbitMQ)

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

#### 5.2.2 Execução do Script Python

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

### 5.3. Entendimento das funcionalidades e configuração do Dashboard

A seguir, descrevemos sobre a utilização e interpretação de cada componente do dashboard desenvolvido. Serão apresentados filtros, alertas, gráficos e indicadores, detalhando a função de cada um e como eles contribuem para o monitoramento eficaz do consumo de rodas e bancos na linha de produção.

#### 5.3.1 Monitoramento da demanda total de bancos na linha de produção

<div align="center">
<sub>Figura 3 - Monitoramento da demanda total de bancos</sub>
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

#### 5.3.1.1 Demanda Atual da linha

<div align="center">
<sub>Figura 4 - Demanda Atual da linha</sub>
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

#### 5.3.1.2 Previsão de demanda diária:

<div align="center">
<sub>Figura 5 - Previsão de demanda diária</sub>
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

#### 5.3.1.3 Relação demanda real vs prevista (%)

<div align="center">
<sub>Figura 6 - Relação demanda real vs prevista (%)</sub>
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

#### 5.3.1.4 Evolução do consumo diário de bancos

<div align="center">
<sub>Figura 7 - Evolução do consumo diário de bancos</sub>
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
<sub>Figura 8 - Alerta Banco</sub>
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
<sub>Figura 9 - Email Alerta</sub>
</div>
<div align="center">
<img src="../../assets/email_alerta.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

#### 5.3.1.5 Consumo mensal de bancos na linha vs limite operacional 

<div align="center">
<sub>Figura 10 - Consumo Mensal de Bancos</sub>
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

#### 5.3.2 Monitoramento da demanda de bancos divida por tipos 

<div align="center">
<sub>Figura 11 - Monitoramento da demanda de bancos divida por tipos</sub>
</div>
<div align="center">
<img src="../../assets/monitoramento_dividido.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

Esta seção do dashboard apresenta a demanda de bancos segmentada por tipo, permitindo uma análise mais detalhada do consumo na linha de produção. Diferentemente da visão geral, aqui o foco está em entender quais tipos de bancos estão sendo mais utilizados, em quais volumes e como esse comportamento evolui ao longo do tempo. Os indicadores e gráficos desta seção possibilitam identificar rapidamente os tipos de bancos com maior demanda atual, comparar volumes consumidos entre diferentes códigos e acompanhar a evolução individual de cada tipo. Essa segmentação é fundamental para apoiar decisões de abastecimento, priorização logística e ajustes no planejamento, especialmente em cenários onde determinados tipos apresentam consumo acima do padrão.

#### 5.3.2.1 Demanda atual da linha por tipo de banco 

<div align="center">
<sub>Figura 12 - Demanda atual da linha por tipo de banco</sub>
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

#### 5.3.2.2 Rancking e tabela dos tipos de bancos mais consumidos nos últimos 14 dias 

<div align="center">
<sub>Figura 13 - Rancking e tabela dos tipos de bancos mais consumidos nos últimos 14 dias</sub>
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


#### 5.3.2.3 Evolução na demanda de cada tipo de banco 

<div align="center">
<sub>Figura 14 - Evolução na demanda de cada tipo de banco </sub>
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

#### 5.3.3 Monitoramento da demanda do banco selecionado 

Um dos features do dashboard é a possibilidade de filtrar todos os gráficos e indicadores para um tipo específico de banco ou roda. Isso é feito por meio de um filtro interativo localizado na parte superior do painel, onde o usuário pode selecionar o código do banco desejado. Ao fazer essa seleção, todos os componentes do dashboard são atualizados automaticamente para refletir apenas os dados relacionados ao banco escolhido.

Essa funcionalidade é especialmente útil para análises detalhadas, permitindo que o usuário foque em um tipo específico de peça e avalie seu comportamento ao longo do tempo, sua demanda atual, evolução e comparação com a previsão. Dessa forma, é possível identificar rapidamente quaisquer desvios ou padrões específicos que possam exigir atenção ou ajustes no planejamento.

<div align="center">
<sub>Figura 15 - Monitoramento da demanda do banco selecionado </sub>
</div>
<div align="center">
<img src="../../assets/analise_demanda_banco_selecionado.png">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

#### 5.3.3.1 Demanda atual do banco selecionado na linha de produção

<div align="center">
<sub>Figura 16 - Demanda atual do banco selecionado na linha de produção </sub>
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

#### 5.3.3.2 Previsão de demanda diária do banco selecionado

Assim como no indicador geral, este painel apresenta a previsão de demanda diária, mas focada exclusivamente no banco selecionado pelo usuário. A previsão é calculada com base na média móvel dos últimos 14 dias completos, excluindo o dia atual para evitar distorções por dados parciais.

<div align="center">
<sub>Figura 17 - Previsão de demanda diária do banco selecionado </sub>
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

#### 5.3.3.3 Relação demanda real vs prevista (%) do banco selecionado

Assim como no indicador geral, este painel apresenta a relação percentual entre a demanda real e a prevista, mas focada exclusivamente no banco selecionado pelo usuário. O indicador é construído a partir da razão entre o consumo real observado no dia e o valor de previsão diária, sendo expresso em percentual.

<div align="center">
<sub>Figura 18 - Relação demanda real vs prevista (%) do banco selecionado </sub>
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

#### 5.3.3.4 Evolução na demanda do banco selecionado ao longo do tempo

<div align="center">
<sub>Figura 19 - Evolução na demanda do banco selecionado ao longo do tempo </sub>
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

#### 5.3.3.5 Consumo mensal do banco selecionado vs limite operacional

<div align="center">
<sub>Figura 20 - Consumo mensal do banco selecionado vs limite operacional </sub>
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

#### 5.3.4 Filtros globais do Dashboard

Na parte superior do dashboard, há dois filtros globais que permitem ao usuário ajustar a visualização dos dados. O primeiro filtro é o seletor de tipo de banco e roda, onde o usuário pode escolher um código específico para analisar. Ao selecionar um tipo, todos os gráficos e indicadores do dashboard são atualizados automaticamente para refletir apenas os dados relacionados ao banco e roda escolhido. O segundo filtro é o seletor de intervalo de datas, que permite ao usuário definir o período de interesse para a análise. Com esse filtro, é possível ajustar o escopo temporal dos dados exibidos, facilitando a comparação entre diferentes períodos ou a visualização de tendências ao longo do tempo. Vale ressaltar que alguns gráficos possuem intervalos fixos definidos em suas consultas SQL, não sendo afetados por esse filtro de data.

#### 5.3.5 Configuração de Alertas no Dashboard

<div align="center">
<sub>Figura 21 - Configuração de Alertas no Dashboard </sub>
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

#### 5.3.6 Dashboard para monitoramento de rodas

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

### 5.4. Conclusão
Nesta seção, detalhamos o processo de verificação do funcionamento do sistema de monitoramento, bem como a estrutura e funcionalidades do dashboard desenvolvido para acompanhar o consumo de bancos e rodas na linha de produção. Foram apresentados os principais indicadores, gráficos e alertas configurados, além da lógica por trás dos cálculos utilizados para gerar essas visualizações. O dashboard foi projetado para oferecer uma visão clara e intuitiva do desempenho operacional, permitindo que os usuários tomem decisões informadas com base em dados atualizados e relevantes. A flexibilidade na configuração de alertas e a possibilidade de filtrar por tipos específicos de bancos e rodas tornam o sistema adaptável às necessidades variadas da operação.



## 6. Testes, Validações e Resultados

### 6.1 Testes de Usabilidade do Dashboard

Foram realizados testes de usabilidade com o dashboard desenvolvido, focados especificamente nos gráficos relacionados ao monitoramento de bancos, contemplando tanto visualizações gerais (total) quanto análises segmentadas por tipo de banco.

#### 6.1.1 Metodologia

A metodologia adotada foi baseada em **teste de tarefas** (task-based testing), onde cada integrante do grupo foi responsável por planejar e executar um teste específico para um gráfico diferente do dashboard, garantindo cobertura abrangente de todas as funcionalidades principais.

**Participantes:**
- 3 participantes por gráfico testado
- Perfis variados: alunos do módulo e técnico de laboratório
- Total de 6 gráficos testados

#### 6.1.2 Gráficos Testados

1. **Consumo diário total x previsão** (Bancos - Visão Geral)
2. **Evolução do consumo total geral** (Bancos - Visão Geral)
3. **Consumo semanal geral** (Bancos - Visão Geral)
4. **Evolução do consumo total por tipo** (Bancos - Análise por Tipo)
5. **Consumo semanal por tipo** (Bancos - Análise por Tipo)
6. **Consumo diário por tipo** (Bancos - Análise por Tipo)

#### 6.1.3 Resultados dos Testes

**Resultado Geral:**
- **83% dos testes completados com sucesso total**
- **17% dos testes completados com dificuldade**

**Taxa de Sucesso por Gráfico:**
- Consumo Diário Total x Previsão: 67% sucesso total, 33% com dificuldade
- Evolução do Consumo Total Geral: 100% completaram todas as tarefas principais, com dificuldades parciais em análises detalhadas (identificação de picos e correlação de informações)
- Consumo Semanal Geral: 67% sucesso total, 33% com dificuldade
- Evolução do Consumo Total por Tipo: **100% sucesso total**
- Consumo Semanal por Tipo: **100% sucesso total**
- Consumo Diário por Tipo: **100% sucesso total**

#### 6.1.4 Pontos Fortes Identificados

1. **Gráficos de Análise por Tipo**: Todos os três gráficos segmentados por tipo apresentaram 100% de sucesso, demonstrando que a segmentação facilita a compreensão e análise.

2. **Cartões de Consumo Diário por Tipo**: O gráfico de consumo diário por tipo foi o mais bem compreendido, com todos os participantes conseguindo localizar valores, comparar números, interpretar cores e justificar respostas com sucesso total.

3. **Medidor Circular**: O medidor circular de consumo diário vs. previsão foi compreendido corretamente, com participantes demonstrando clara compreensão da relação entre consumo real e previsão.

4. **Gráficos de Barras Ordenadas**: O gráfico de tipos mais consumidos por período facilitou a identificação de rankings, com todos conseguindo identificar posições específicas sem dificuldades.

#### 6.1.5 Dificuldades Encontradas

1. **Interpretação de Datas/Dias da Semana**: Dificuldade em interpretar as datas/dias da semana no gráfico de consumo semanal geral.

2. **Inconsistência de Valores**: Valores inconsistentes no gráfico de consumo diário total x previsão, dificultando a interpretação correta.

3. **Identificação de Picos em Gráficos de Linha**: Dificuldade para encontrar picos corretos em gráficos de linha temporal.

#### 6.1.6 Recomendações de Melhoria

**Alta Prioridade:**
- Melhorar clareza na representação de datas/dias da semana
- Validar e corrigir inconsistências de valores
- Adicionar tooltips e textos de ajuda

**Média Prioridade:**
- Melhorar destaque de picos em gráficos de linha
- Melhorar legenda das faixas de referência
- Adicionar guia rápido de uso

### 6.2 Validação do Modelo de Otimização

O modelo de otimização de supply chain foi validado através de:

#### 6.2.1 Teste com Dados Reais

- Utilização de dados reais de dois meses de produção da Volkswagen
- Cálculo de demandas mínima e máxima a partir de histórico
- Execução do solver PuLP com resultado: **Status: Ótimo**

#### 6.2.2 Validação das Restrições

A solução encontrada respeitou todas as restrições:
- Estoque total (84 rodas) ≤ Capacidade máxima (4.096 rodas)
  - Cálculo: (16 + 36 + 32) = 84 ≤ 4.096
- Cada tipo de roda dentro dos limites de demanda mínima e máxima
  - Tipo 41P: x1_min ≤ 16 ≤ 136 (demanda máxima)
  - Tipo C0V: x2_min ≤ 36 ≤ 128 (demanda máxima)
  - Tipo CR4: x3_min ≤ 32 ≤ 168 (demanda máxima)
- Solução alinhada com princípios JIT/JIS

#### 6.2.3 Análise de Sensibilidade

Foram testados três cenários:

1. **Redução da capacidade de estoque**: Modelo não sensível nas condições atuais
2. **Aumento das demandas mínimas**: Modelo ajusta valores proporcionalmente
3. **Alteração no mix de produção**: Modelo responde de forma coerente às mudanças

### 6.3 Validação da Arquitetura

A arquitetura foi validada através de:

#### 6.3.1 Validação com Stakeholders

- **Equipe de Automação**: Validação de padrão corporativo Siemens (Referência 8)
- **Equipe de Produção**: Confirmação de custo de parada e aceitação de meta de redução
- **Equipe de Qualidade**: Confirmação de especificação técnica de sensores
- **Equipe de Manutenção**: Validação de experiência positiva com fornecedores
- **Equipe de Compras**: Confirmação de processos de ex-tarifário e disponibilidade
- **Equipe de TI**: Validação de capacidade técnica do PowerHA (Referência 6)
- **Equipe Financeira**: Validação de ROI e payback estimados

#### 6.3.2 Validação Técnica

- **Capacidade de Processamento**: Arquitetura dimensionada para 50.000+ eventos/hora
- **Redundância**: Configuração N+1 validada para pontos críticos
- **Protocolos**: OPC-UA e MQTT validados como padrão da indústria

---

## 7. Análise de Impacto e Viabilidade

### 7.1 Impacto Operacional

#### 7.1.1 Redução de Paradas Não Programadas

**Benefício Mensurável:**
- **Redução de 95% no risco de parada não programada** (de 4 eventos/ano para 0,2 eventos/ano)
- **Economia estimada: R$ 4.800.000/ano** (evitar 40 minutos de parada/ano)

**Mecanismo:**
- Redundância N+1 (PLCs S7-1500) (Referência 8) e Cluster PowerHA (Servidores IBM) (Referência 6)
- Sistema de alertas proativos que notifica sobre estoque baixo antes da falta
- Previsão de consumo baseada em histórico permite garantir disponibilidade da peça correta no momento da montagem

**Redução de Retrabalho:**
A solução diminui podendo até eliminar a necessidade de uso de peças reserva temporárias. Atualmente, quando não há a peça necessária para um carro específico, utiliza-se uma peça "reserva" que serve apenas como apoio temporário para evitar paradas na linha de produção, gerando retrabalho posterior para substituição pela peça correta. Com o sistema de alertas proativos e previsão de consumo, a peça correta estará disponível no momento necessário, eliminando esse retrabalho e aumentando a eficiência operacional.

#### 7.1.2 Eliminação de Recalls por Falha de Torque

**Benefício Mensurável:**
- **Redução de 90% em defeitos de torque** (de 0,1% para 0,01% de veículos)
- **Eliminação de recalls por falha de torque** (economia estimada: R$ 50.000.000/ano)

**Mecanismo:**
- Sensores HBM T10F de alta precisão (qualidade de laboratório) (Referência 10)
- Atuadores Atlas Copco com controle preciso de torque

#### 7.1.3 Redução de Manutenção Corretiva

**Benefício Mensurável:**
- **Redução de 60% em manutenção corretiva** (de 12 eventos/ano para 5 eventos/ano)
- **Conversão de 80% das paradas não programadas em paradas programadas**
- **Economia estimada: R$ 1.200.000/ano** (redução de 10 horas de parada/ano)

**Mecanismo:**
- Sensores de vibração/temperatura IFM para manutenção preditiva
- Detecção de falhas incipientes antes da quebra

#### 7.1.4 Rastreabilidade Unívoca

**Benefício Mensurável:**
- **100% de rastreabilidade** de componentes (roda, banco) e parâmetros de qualidade (torque) associados ao VIN
- **Redução de 70% no tempo de investigação de problemas de campo** (de 2 semanas para 3 dias)
- **Economia estimada: R$ 550.000/ano** (economia de 11 semanas/ano)

**Mecanismo:**
- Leitores SICK UHF/QR Code em pontos críticos (M100, Tacto 123/127, G700) (Referência 9)
- Associação de cada componente ao número de chassi (VIN)

#### 7.1.5 Redução de Capital de Giro

**Benefício Mensurável:**
- **Redução de 40% no lead time médio** de reposição (de 90 dias para 30 dias)
- **Redução de R$ 500.000 em estoque de segurança** necessário
- **Economia estimada: R$ 75.000/ano** (custo de oportunidade)

**Mecanismo:**
- Componentes com estoque local (60% do volume): Balluff, IFM, Atlas Copco
- Redução de dependência cambial e lead times

### 7.2 Resumo Executivo de Benefícios

| Categoria de Benefício | Impacto Quantitativo | Valor Estimado (R$/ano) |
|------------------------|---------------------|-------------------------|
| **Redução de Paradas Não Programadas** | 95% de redução (40 minutos/ano evitados) | R$ 4.800.000 |
| **Eliminação de Recalls por Falha de Torque** | 100% de eliminação | R$ 50.000.000 |
| **Redução de Manutenção Corretiva** | 60% de redução (10 horas/ano evitadas) | R$ 1.200.000 |
| **Redução de Capital de Giro (Estoque)** | R$ 500.000 em estoque reduzido | R$ 75.000 |
| **Redução de Tempo de Investigação de Qualidade** | 70% de redução (economia de 11 semanas/ano) | R$ 550.000 |
| **TOTAL DE BENEFÍCIOS OPERACIONAIS** | | **R$ 56.625.000/ano** |

### 7.3 Análise de Viabilidade Econômica

#### 7.3.1 Custos de Implementação

**Investimento Inicial (CAPEX):**
- **Cenário Conservador**: R$ 200.000,00 (utilizado para análise financeira)
- **Cenário Realista Industrial**: R$ 3.067.479,00 (arquitetura completa)

**Cronograma de Desembolso (18 meses):**
- Meses 1-3: Servidores IBM Power (Master + Mirror) + Licenças IBM (PowerHA + DB2) = R$ 1.965.000
- Meses 4-6: PLCs Siemens (S7-1500 + S7-1200) + Sensores HBM (Torque) = R$ 373.755
- Meses 7-9: Sensores Balluff, IFM, Atlas Copco + Leitores SICK UHF = R$ 383.724
- Meses 10-12: Switches, Gateways, Cabos = R$ 45.000
- Meses 13-15: Integração e Testes = R$ 200.000
- Meses 16-18: Comissionamento e Go-Live = R$ 100.000

**Total CAPEX:** R$ 3.067.479,00
(Verificação: R$ 1.965.000 + R$ 373.755 + R$ 383.724 + R$ 45.000 + R$ 200.000 + R$ 100.000 = R$ 3.067.479)

#### 7.3.2 Análise Financeira (Cenário Conservador)

**Premissas:**
- Investimento: R$ 200.000,00
- Tempo de Payback Desejado: 4 meses
- Lucro Mensal Mínimo: R$ 50.000,00
- Taxa de Juros: 15% a.a. (1,171% a.m.)
- TMA: 12% a.a. (0,95% a.m.)

**Resultados:**

**ROI (Return on Investment):**

Para o cálculo do ROI, considerou-se um horizonte de análise de **12 meses**, onde o projeto deve gerar o lucro mensal mínimo de R$ 50.000,00 estabelecido nas premissas.

**Cálculo do Ganho Total:**
- Lucro Mensal Mínimo: R$ 50.000,00
- Horizonte de Análise: 12 meses
- **Ganho Total (12 meses)**: R$ 50.000,00 × 12 = **R$ 600.000,00**

**Cálculo do ROI:**
```
ROI = (Ganho Total - Investimento) / Investimento
ROI = (R$ 600.000 - R$ 200.000) / R$ 200.000
ROI = R$ 400.000 / R$ 200.000
ROI = 200%
```

**Interpretação**: A cada R$ 1 investido, a Volkswagen terá R$ 2 de lucro (fora o valor inicial), considerando um período de 12 meses de operação.

**VPL (Valor Presente Líquido):**
- **VPL Total: R$ 364.535,77**
- Como o VPL é > 0, o projeto gera valor econômico

**TIR (Taxa Interna de Retorno):**
- **TIR aproximada: 65% a 70% a.a.**
- TIR muito superior à TMA de 12% a.a., indicando projeto altamente lucrativo

**Payback:**
- **Payback: 4 meses** (conforme objetivo estabelecido)

#### 7.3.3 Análise Financeira (Cenário Realista Industrial)

**Premissas:**
- Investimento: R$ 3.067.479,00
- Benefícios Anuais: R$ 56.625.000,00

**Resultados:**

**Cálculo do ROI:**
```
ROI = (Ganho Total - Investimento) / Investimento
ROI = (R$ 56.625.000 - R$ 3.067.479) / R$ 3.067.479
ROI = R$ 53.557.521 / R$ 3.067.479
ROI = 17,45
ROI = 1.745%
```

**Payback:**
```
Payback = R$ 3.067.479 / R$ 56.625.000
Payback = 0,05 anos (18 dias)
```

### 7.4 Impacto Estratégico

#### 7.4.1 Alinhamento com Indústria 4.0

O projeto posiciona a Volkswagen do Brasil como referência em:
- Digitalização de processos produtivos
- Implementação de IoT industrial
- Uso de dados para tomada de decisão estratégica

#### 7.4.2 Melhoria de Competitividade

- **Redução de custos operacionais**: R$ 56.625.000/ano em benefícios mensuráveis
- **Aumento de eficiência**: Redução de 95% em paradas não programadas
- **Melhoria de qualidade**: Eliminação de recalls por falha de torque

#### 7.4.3 Base para Expansão

A arquitetura desenvolvida serve como base para:
- Expansão para outras linhas de produção
- Integração com sistemas corporativos (SAP/MES)
- Implementação de Machine Learning para previsão avançada

---

## 8. Instruções de Uso e Implantação

### 8.1 Requisitos para Execução

#### 8.1.1 Requisitos de Hardware

- **Servidores IBM Power Systems** (Master + Mirror) com capacidade para 50.000+ eventos/hora
- **PLCs Siemens S7-1500/1200** conforme especificação da arquitetura
- **Sensores e Leitores** conforme BOM (Bill of Materials)
- **Infraestrutura de Rede** cabeada TCP/IP industrial

#### 8.1.2 Requisitos de Software

- **Node.js 18+** (para orquestração/local tooling)
- **Python 3.10+** (scripts e utilitários)
- **Docker 24+** (opcional; facilita execução de serviços)
- **IBM DB2** (banco de dados corporativo)
- **Node-RED** (middleware de orquestração IoT)

#### 8.1.3 Requisitos de Infraestrutura

- **Rede Industrial** com VLANs segregadas (OT, TI, DMZ)
- **Firewall** entre camadas OT e TI
- **Certificados X.509** para autenticação MQTT

### 8.2 Processo de Implantação

#### 8.2.1 Fase 1: Preparação (Meses 1-3)

1. **Aquisição de Componentes:**
   - Servidores IBM Power (lead time: 90-180 dias)
   - Licenças IBM (PowerHA + DB2)

2. **Preparação de Infraestrutura:**
   - Configuração de VLANs
   - Instalação de firewall
   - Preparação de ambiente de servidores

#### 8.2.2 Fase 2: Instalação de Hardware OT (Meses 4-9)

1. **Instalação de Sensores e Leitores:**
   - Leitores UHF SICK RFU620 (M100, Tacto 123, Tacto 127, G700)
   - Sensores de torque HBM T10F (Tacto 123)
   - Sensores de posicionamento Balluff BTL
   - Sensores de vibração IFM/VSA
   - Atuadores Atlas Copco Tensor DS

2. **Instalação de CLPs:**
   - PLCs Siemens S7-1500 (Tacto 123, Supervisão, Redundância)
   - PLCs Siemens S7-1200 (M100, Tacto 127, G700)

3. **Instalação de Infraestrutura de Rede:**
   - Switches industriais Siemens Scalance
   - Gateways OT/TI Siemens IOT2050
   - Cabeamento industrial TCP/IP

#### 8.2.3 Fase 3: Configuração de Software (Meses 10-12)

1. **Configuração de Middleware:**
   - Instalação e configuração de Node-RED
   - Desenvolvimento de flows para processamento de dados
   - Configuração de integração MQTT, responsável por estabelecer a comunicação entre os dispositivos e o broker.

2. **Configuração de Banco de Dados:**
   - Instalação e configuração de DB2
   - Criação de esquemas de dados
   - Configuração de backup e redundância

3. **Desenvolvimento do Dashboard:**
   - O dashboard se baseia em uma arquitetura orientada a eventos, representada pelo seguinte fluxo: **Sensores / Eventos → Fila (RabbitMQ) → Python → PostgreSQL → Grafana**
   - Cada componente tem um papel específico: a fila garante resiliência e desacoplamento; o script Python processa e valida os dados; o banco de dados organiza as informações para consulta eficiente; o Grafana consome os dados já tratados e agregados
   - **Conexão com a Fila (RabbitMQ)**: A fila RabbitMQ atua como o ponto central de entrada dos eventos da linha de produção. Nenhum dado é enviado diretamente ao banco: tudo passa primeiro pela fila. Isso garante que eventos não sejam perdidos, o sistema suporte picos de mensagens e o processamento possa ser pausado ou reiniciado sem impacto nos sensores
   - **Execução do Script Python**: O script Python `modulo-conexao-iot.py` localizado na pasta `src` é responsável por ligar a fila ao banco de dados. Ele executa continuamente: conexão ao RabbitMQ, consumo de mensagens da fila, interpretação e validação dos dados recebidos, inserção dos dados no PostgreSQL
   - **Configuração do ambiente**: O script utiliza variáveis de ambiente para realizar a conexão tanto com a fila RabbitMQ quanto com o banco de dados PostgreSQL. É obrigatória a criação de um arquivo `.env` na raiz do projeto para armazenar todas as configurações sensíveis de conexão
   - **Funcionalidades do Dashboard**: O dashboard permite tanto uma visualização geral do consumo, quanto uma análise detalhada por tipo de peça, possibilitando identificar rapidamente quaisquer desvios entre o consumo real e o previsto, além de destacar áreas que necessitam de atenção imediata. Foram também configurados alertas para que o usuário não deixe passar despercebido quando os limites críticos forem atingidos

#### 8.2.4 Fase 4: Integração e Testes (Meses 13-15)

1. **Integração de Componentes:**
   - Teste de comunicação OPC-UA entre PLCs e Gateways
   - Teste de comunicação MQTT entre Gateways e Node-RED
   - Teste de integração REST com sistemas legados

2. **Testes Funcionais:**
   - Validação de coleta de dados dos sensores
   - Validação de processamento no Node-RED
   - Validação de armazenamento no DB2
   - Validação de visualização no Dashboard

3. **Testes de Performance:**
   - Validação de capacidade de 50.000+ eventos/hora
   - Validação de latência < 200ms (p95)
   - Validação de tempo de recuperação < 500ms

#### 8.2.5 Fase 5: Comissionamento e Go-Live (Meses 16-18)

1. **Treinamento de Usuários:**
   - Treinamento para Analistas de Logística
   - Treinamento para Gerentes de Estoque
   - Treinamento para Supervisores de Logística
   - Treinamento para Representantes de Fornecedores

2. **Go-Live:**
   - Ativação gradual do sistema
   - Monitoramento intensivo nas primeiras semanas
   - Ajustes finos baseados em feedback dos usuários

### 8.3 Instruções de Uso do Sistema

#### 8.3.1 Acesso ao Dashboard

O dashboard se baseia em uma arquitetura orientada a eventos, representada pelo seguinte fluxo:

**Sensores / Eventos → Fila (RabbitMQ) → Python → PostgreSQL → Grafana**

Cada componente tem um papel específico:
- A fila garante resiliência e desacoplamento;
- O script Python processa e valida os dados;
- O banco de dados organiza as informações para consulta eficiente;
- O Grafana consome os dados já tratados e agregados.

**Antes de acessar o dashboard, é necessário:**

- RabbitMQ Server instalado e em execução
- Python 3.10 ou superior
- Acesso à fila configurada (host, porta, usuário e senha)
- PostgreSQL configurado e acessível
- Grafana instalado e configurado

**Configuração do ambiente:**

O script utiliza **variáveis de ambiente** para realizar a conexão tanto com a fila RabbitMQ quanto com o banco de dados PostgreSQL.

Antes de executar o sistema, certifique-se de configurar corretamente o arquivo `.env` na raiz do projeto, seguindo a estrutura:

```env
# ==================== CONFIGURAÇÃO RABBITMQ ====================
RABBITMQ_HOST=SEU_HOST_AQUI
RABBITMQ_PORT=5672
RABBITMQ_USER=SEU_USUARIO
RABBITMQ_PASS=SUA_SENHA
RABBITMQ_QUEUE=NOME_DA_FILA
RABBITMQ_HEARTBEAT=600
RABBITMQ_BLOCKED_TIMEOUT=300

# ==================== CONFIGURAÇÃO DO BANCO DE DADOS ====================
SUPABASE_DB_URL=POSTGRESQL_CONNECTION_STRING
SUPABASE_SCHEMA=public
SCHEMA_FILE=schema.sql

# ==================== CONFIGURAÇÃO DE TABELA ====================
DB_TABLE_NAME=telemetry_professor
STAGE_TIMESTAMP_COLUMNS=M100,M200,M215,M244,M252,M282,M310,M313,G700
```

**Iniciando o sistema:**

No diretório raiz do projeto, execute:

```bash
python modulo-conexao-iot.py
```
Após iniciado, o script:
- Passa a escutar continuamente a fila RabbitMQ;
- Processa automaticamente novos eventos recebidos;
- Não requer intervenção manual durante a operação normal.

**Acesso ao Dashboard Grafana:**

Após o sistema estar em execução e processando dados:
1. Acesse o Grafana através do navegador web
2. Faça login com suas credenciais
3. Navegue até o painel do dashboard de monitoramento de consumo
4. O dashboard será atualizado automaticamente conforme novos dados são processados

**Validação do funcionamento:**

Para confirmar que o sistema está operando corretamente:
- Verifique se novas linhas estão sendo inseridas na tabela de telemetria;
- Observe se a fila começa a esvaziar após o processamento;
- Confirme que não há erros de conexão ou exceções no terminal;
- Verifique se os gráficos do dashboard estão sendo atualizados com dados recentes.

#### 8.3.2 Interpretação de Alertas

O sistema utiliza um esquema de cores para indicar níveis de estoque:

- **Verde**: Estoque dentro do nível seguro
- **Amarelo**: Estoque próximo ao nível mínimo - atenção necessária
- **Vermelho**: Estoque crítico - ação imediata necessária

#### 8.3.3 Geração de Relatórios

O dashboard Grafana oferece funcionalidades nativas para geração de relatórios e exportação de dados:

**Exportação de Dados:**

1. **Exportação de Gráficos**: Cada gráfico do dashboard possui opções de exportação, permitindo salvar visualizações em formatos como PNG, PDF ou CSV
2. **Exportação de Dados Brutos**: É possível exportar os dados subjacentes de qualquer gráfico através da opção "Export CSV" disponível no menu de cada painel
3. **Exportação de Painel Completo**: O dashboard completo pode ser exportado como PDF através da opção "Share" → "PDF" no menu superior do Grafana

**Geração de Relatórios Automatizados:**

O Grafana permite configurar relatórios agendados que são enviados automaticamente por e-mail:

1. Acesse a opção "Alerting" → "Notification channels" no Grafana
2. Configure um canal de notificação por e-mail
3. Crie alertas ou relatórios agendados que utilizem esse canal
4. Defina a frequência de envio (diário, semanal, mensal)

**Relatórios Personalizados:**

Para relatórios mais específicos ou análises detalhadas:

1. Utilize as consultas SQL diretamente no banco de dados PostgreSQL
2. Os dados estão organizados nas tabelas `bank_hourly_matrix` e `wheel_hourly_matrix`
3. É possível criar consultas personalizadas para análises específicas conforme necessário
4. Os dados podem ser exportados e processados em ferramentas externas (Excel, Power BI, etc.)

**Dados Disponíveis para Relatórios:**

- Consumo diário de bancos e rodas
- Consumo por tipo de componente
- Evolução temporal do consumo
- Previsões de demanda
- Relação entre consumo real e previsto
- Alertas e eventos críticos registrados

### 8.4 Manutenção e Suporte

#### 8.4.1 Manutenção Preventiva

- **Calibração de Sensores**: Sensores de torque HBM requerem calibração periódica (conforme especificação do fabricante)
- **Atualização de Software**: Node-RED e componentes de software devem ser atualizados regularmente
- **Backup de Dados**: Backups automáticos do DB2 devem ser verificados regularmente

#### 8.4.2 Suporte Técnico

- **Siemens Brasil**: Suporte técnico 24/7 para CLPs e gateways
- **IBM Brasil**: Suporte técnico 24/7 para servidores e banco de dados
- **Fornecedores de Sensores**: Suporte técnico conforme contratos de manutenção

---

## 9. Limitações, Riscos e Considerações Finais

### 9.1 Limitações do Projeto

#### 9.1.1 Limitações de Escopo (MVP)

O projeto foi desenvolvido como MVP (Minimum Viable Product), com as seguintes limitações:

1. **Integração Limitada com Sistemas Corporativos:**
   - Não há integração direta com SAP/MES no escopo inicial
   - Integração realizada através de APIs REST, permitindo expansão futura

2. **Cobertura Inicial:**
   - Foco inicial em rodas e bancos
   - Expansão para outros componentes requer implementação adicional

3. **Histórico de Dados:**
   - Dashboard utiliza dados dos últimos 2 meses (conforme TAPI)
   - Expansão do histórico requer ajustes na arquitetura de armazenamento

#### 9.1.2 Limitações Técnicas

1. **Dependência de Importação:**
   - Componentes críticos (HBM T10F) requerem importação direta (lead time: 90-120 dias)
   - Impacto cambial pode afetar custos do projeto

2. **Complexidade de Integração:**
   - Integração com sistemas legados requer conhecimento técnico especializado
   - Mudanças em sistemas legados podem impactar integrações

3. **Capacidade de Processamento:**
   - Arquitetura dimensionada para 50.000+ eventos/hora
   - Expansão significativa pode requerer upgrade de infraestrutura

### 9.2 Riscos Identificados

#### 9.2.1 Riscos Técnicos

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| **Falha de Hardware Crítico** | Baixa | Alto | Redundância N+1 em pontos críticos, Cluster PowerHA |
| **Falha de Comunicação OT/TI** | Média | Alto | Rede cabeada, redundância de switches, monitoramento 24/7 |
| **Incompatibilidade de Protocolos** | Baixa | Médio | Uso de protocolos padrão da indústria (OPC-UA, MQTT) |
| **Perda de Dados** | Baixa | Alto | Backup automático DB2, espelhamento síncrono |

#### 9.2.2 Riscos Operacionais

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| **Resistência à Mudança** | Média | Médio | Treinamento adequado, envolvimento de usuários no desenvolvimento |
| **Curva de Aprendizado** | Alta | Baixo | Interface intuitiva, suporte técnico dedicado |
| **Dependência de Fornecedores** | Média | Médio | Contratos com SLAs, múltiplos fornecedores quando possível |

#### 9.2.3 Riscos Financeiros

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| **Variação Cambial** | Alta | Alto | Compra antecipada quando possível, hedge cambial |
| **Aumento de Custos de Importação** | Média | Médio | Busca por regimes especiais (ex-tarifário), componentes locais quando possível |
| **Atraso na Implementação** | Média | Médio | Planejamento rigoroso, estoque de segurança para componentes críticos |

### 9.3 Considerações Finais

#### 9.3.1 Sucessos do Projeto

O projeto alcançou os seguintes sucessos:

1. **Arquitetura Completa e Validada:**
   - Arquitetura IoT de três camadas completamente especificada
   - Validação técnica com stakeholders internos da Volkswagen
   - Especificações técnicas detalhadas para implementação

2. **Viabilidade Econômica Demonstrada:**
   - ROI de 200% (cenário conservador) ou 1.745% (cenário realista)
   - Payback de 4 meses (cenário conservador) ou 18 dias (cenário realista)
   - Benefícios anuais estimados em R$ 56.625.000

3. **Validação de Usabilidade:**
   - 83% dos testes de usabilidade completados com sucesso total
   - Gráficos de análise por tipo com 100% de sucesso
   - Interface considerada intuitiva pelos usuários

4. **Modelo de Otimização Funcional:**
   - Modelo de otimização de supply chain validado com dados reais
   - Solução ótima encontrada respeitando todas as restrições
   - Alinhamento com princípios JIT/JIS

#### 9.3.2 Lições Aprendidas

1. **Importância da Validação com Stakeholders:**
   - Envolvimento de stakeholders desde o início garantiu alinhamento com necessidades reais
   - Validação técnica evitou retrabalho e garantiu viabilidade

2. **Benefícios da Abordagem Incremental:**
   - Desenvolvimento em sprints permitiu validação contínua
   - Ajustes foram feitos de forma ágil baseados em feedback

3. **Relevância do Benchmarking:**
   - Estudo de casos de referência (Hyundai, Amazon, BYD) forneceu insights valiosos para elaboração do benchmarking, fundamentando pontos focais de avaliação
   - Adaptação de melhores práticas ao contexto da Volkswagen

#### 9.3.3 Desafios Enfrentados

1. **Complexidade da Arquitetura:**
   - Integração de múltiplas camadas (OT, TI) requer conhecimento técnico especializado
   - Solução: Trabalho colaborativo entre equipes técnicas

2. **Dependência de Importação:**
   - Componentes críticos requerem importação com lead times extensos
   - Solução: Planejamento antecipado, estoque de segurança, busca por componentes locais

3. **Custos Elevados:**
   - Investimento inicial significativo (R$ 3.067.479 no cenário realista)
   - Solução: Demonstração clara de ROI e benefícios operacionais

---

## 10. Possibilidades de Evolução Futura

### 10.1 Expansão de Funcionalidades

#### 10.1.1 Integração com Sistemas Corporativos

**Integração com SAP/MES:**
- Expansão do MVP para integração direta com sistemas corporativos
- Sincronização bidirecional de dados de produção e estoque
- Eliminação de redundância de dados e processos manuais

**Integração com Sistemas de Qualidade:**
- Integração mais profunda com sistemas CobrA
- Análise automática de não conformidades
- Rastreabilidade completa de causas-raiz de defeitos

#### 10.1.2 Expansão de Cobertura

**Outros Componentes:**
- Expansão do monitoramento para outros componentes críticos da linha de montagem
- Aplicação da mesma arquitetura para diferentes estações de trabalho
- Criação de visão consolidada de toda a linha de produção

**Múltiplas Linhas:**
- Expansão para outras linhas de montagem da fábrica
- Comparação de performance entre linhas
- Otimização global da produção

### 10.2 Tecnologias Avançadas

#### 10.2.1 Inteligência Artificial e Machine Learning

**Previsão Avançada de Demanda:**
- Implementação de modelos de Machine Learning para previsão de consumo, após filtro geral de modelos com maior proeficiência
- Consideração de fatores externos (sazonalidade, campanhas de marketing, etc.)
- Otimização automática de níveis de estoque

**Manutenção Preditiva Avançada:**
- Análise de padrões de vibração e temperatura para previsão de falhas
- Alertas proativos para manutenção antes de falhas críticas
- Otimização de cronogramas de manutenção

**Análise de Causa-Raiz Automatizada:**
- Uso de IA para identificar padrões em dados de qualidade
- Correlação automática entre defeitos e parâmetros de processo
- Sugestões automáticas de ações corretivas

#### 10.2.2 Digital Twin

**Modelo Digital da Linha de Produção:**
- Criação de réplica digital completa da linha de montagem
- Simulação de cenários de produção e testes de estresse 
- Otimização de layout e fluxo de materiais

**Simulação de Cenários:**
- Teste de mudanças de processo sem impacto na produção real
- Mapeamento de impacto sistêmico nas abordagens utilizadas em toda a linha
- Validação de melhorias antes da implementação
- Treinamento de operadores em ambiente virtual

### 10.3 Melhorias de Performance

#### 10.3.1 Otimização de Latência

**Processamento em Edge:**
- Processamento de dados críticos diretamente nos gateways
- Redução de latência para alertas em tempo real
- Menor dependência de comunicação com servidores centrais

**Otimização de Queries:**
- Otimização de consultas ao banco de dados
- Uso de índices e particionamento de tabelas
- Cache de dados frequentes

#### 10.3.2 Escalabilidade

**Arquitetura Distribuída:**
- Distribuição de processamento entre múltiplos servidores
- Balanceamento de carga para alta disponibilidade
- Escalabilidade horizontal para crescimento futuro

**Cloud Computing:**
- Migração de componentes não críticos para cloud
- Redução de custos de infraestrutura
- Flexibilidade para picos de demanda

### 10.4 Expansão de Análises

#### 10.4.1 Análise Preditiva Avançada

**Previsão de Tendências:**
- Análise de tendências de longo prazo
- Identificação de padrões sazonais e integração com planejamento estratégico de mercado 

**Otimização de Mix de Produção:**
- Análise de rentabilidade por modelo de veículo
- Otimização de mix de produção para maximizar lucro
- Consideração de restrições de capacidade e demanda

#### 10.4.2 Business Intelligence

**Dashboards Executivos:**
- Dashboards de alto nível para diretoria
- KPIs consolidados e métricas estratégicas
- Análise de performance histórica e projeções futuras

**Relatórios Automatizados:**
- Geração automática de relatórios periódicos
- Distribuição automática para stakeholders
- Análise comparativa entre períodos

### 10.5 Integração com Ecossistema IoT

#### 10.5.1 Expansão de Sensores

**Novos Tipos de Sensores:**
- Sensores de temperatura ambiente
- Sensores de umidade
- Sensores de qualidade do ar
- Sensores de energia elétrica

**Sensores Wearables:**
- Monitoramento de saúde e segurança dos operadores
- Rastreamento de movimentação para otimização de layout
- Análise de ergonomia e prevenção de acidentes

#### 10.5.2 Conectividade Avançada

**5G Industrial:**
- Implementação de rede 5G para comunicação ultra-rápida
- Redução de latência para aplicações críticas
- Maior capacidade para múltiplos dispositivos IoT

**Edge Computing:**
- Processamento de dados na borda da rede
- Redução de latência e uso de banda
- Maior resiliência a falhas de comunicação

### 10.6 Sustentabilidade e Eficiência Energética

#### 10.6.1 Monitoramento de Consumo Energético

**Análise de Consumo:**
- Monitoramento de consumo energético por estação
- Identificação de oportunidades de economia
- Otimização de horários de operação

**Gestão de Recursos:**
- Otimização de uso de recursos (água, ar comprimido, etc.)
- Redução de desperdícios
- Alinhamento com objetivos de sustentabilidade

---

## 11. Referências

### 11.1 Referências Bibliográficas

**Referência 1.** ALSHAHRANI, S. T. Industry 4.0 in "Major Emerging Markets": A Systematic Literature Review of Benefits, Use, Challenges, and Mitigation Strategies in Supply Chain Management. *Sustainability*, v. 15, n. 20, art. 14811, 2023. Disponível em: <https://www.mdpi.com/2071-1050/15/20/14811>. Acesso em: 22 out. 2025.

**Referência 2.** ALSAADI, N. Modeling and Analysis of Industry 4.0 Adoption Challenges in the Manufacturing Industry. *Processes*, v. 10, n. 10, art. 2150, 2022. Disponível em: <https://www.mdpi.com/2227-9717/10/10/2150>. Acesso em: 22 out. 2025.

**Referência 3.** KALSOOM, T.; AHMED, S.; RAFI-UL-SHAN, P. M.; AZMAT, M.; AKHTAR, P.; PERVEZ, Z.; IMRAN, M. A.; UR-REHMAN, M. Impact of IoT on Manufacturing Industry 4.0: A New Triangular Systematic Review. *Sustainability*, v. 13, n. 22, art. 12506, 2021. Disponível em: <https://www.mdpi.com/2071-1050/13/22/12506>. Acesso em: 22 out. 2025.

**Referência 4.** OSTERWALDER, Alex et al. Value Proposition Design: How to Create Products and Services Customers Want. 1. ed. New Jersey: John Wiley & Sons, 2014.

**Referência 5.** SAS Institute. Industry 4.0 – the fourth industrial revolution. SAS Insights. Disponível em: <https://www.sas.com/pt_br/insights/big-data/industry-4-0.html>. Acesso em: 22 out. 2025.

### 11.2 Documentação Técnica

**Referência 6.** IBM. Documentação técnica PowerHA - Guia de Alta Disponibilidade, 2024. Disponível em: <https://www.ibm.com/docs/pt/i/7.4.0?topic=availability-implementing-high>. Acesso em: jan. 2026.

**Referência 7.** Node-RED. Documentação oficial. Disponível em: <https://nodered.org/docs/>. Acesso em: dez. 2025.

**Referência 8.** Siemens. Documentação técnica S7-1500/1200 - Manual de Sistema, 2024. Disponível em: <https://cache.industry.siemens.com/dl/files/115/82212115/att_108330/v2/82212115_s7_communication_s7-1500_en.pdf>. Acesso em: jan. 2026.

**Referência 9.** SICK. Documentação técnica RFU620 - Manual do Usuário, 2024. Disponível em: <https://www.sick.com/media/docs/2/92/492/operating_instructions_rfu62x_pt_im0056492.pdf>. Acesso em: jan. 2026.

**Referência 10.** HBM. Documentação técnica T10F - Especificações Técnicas, 2024. Disponível em: <https://www.hbm.com/pt/2379/t10f-medidor-de-torque-com-design-extremamente-baixo/>. Acesso em: jan. 2026.

### 11.3 Documentos do Projeto

**Referência 11.** TAPI VW 2025. 1. ed. São Paulo, SP: Volkswagen, 2025. Acesso em: 22 out. 2025.

**Referência 12.** Time Sem Parar. Canvas de Proposta de Valor. Sprint 1, 2025.

**Referência 13.** Time Sem Parar. Personas e Jornadas de Usuário. Sprint 1, 2025.

**Referência 14.** Time Sem Parar. Arquitetura IoT do Projeto. Sprint 2, 2025.

**Referência 15.** Time Sem Parar. Otimização de Supply Chain. Sprint 2, 2025.

**Referência 16.** Time Sem Parar. KPIs Operacionais e Econômicos. Sprint 3, 2025.

**Referência 17.** Time Sem Parar. Benchmarking. Sprint 3, 2025.

**Referência 18.** Time Sem Parar. EVTE, ROI, VPL e TIR. Sprint 4, 2025.

**Referência 19.** Time Sem Parar. Bill of Materials (BOM). Sprint 4, 2025.

**Referência 20.** Time Sem Parar. Relatório de Testes de Usabilidade. Sprint 5, 2025.

### 11.4 Normas e Padrões

**Referência 21.** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. Sistemas RFID – Especificações Gerais. ABNT NBR 17070.

**Referência 22.** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. Sistemas de Comunicação Industrial — Requisitos EMC. ABNT NBR IEC 61000.

**Referência 23.** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. Informação e documentação - Referências - Elaboração. ABNT NBR 6023:2018.

---

**Elaborado por**: Time Sem Parar  
**Data**: Dezembro de 2025
**Versão**: 1.0

---
