## 1. Definição da Arquitetura, Componentes e Funcionalidades

### 1.1. Descrição dos Componentes Principais (Camadas)

#### 1.1.1. Camada de Percepção e Controle (OT - Chão de Fábrica)

&nbsp;&nbsp;&nbsp;&nbsp;A base da arquitetura no chão de fábrica é composta por sensores de identificação, medição e Controladores Lógicos Programáveis (CLPs). A arquitetura é robusta, focada na inspeção, rastreabilidade e no controle de qualidade da montagem de rodas (Tacto 123) e bancos (Tacto 127).

&nbsp;&nbsp;&nbsp;&nbsp;O controle e a consolidação dos dados dos sensores são feitos pelos CLPs. A marca *Siemens (Simatic)* é o padrão inegociável, utilizando-se modelos modernos como o *S7-1200/1500. Para pontos críticos (Tacto 123), o sistema emprega **PLCs redundantes em configuração N+1* para garantir failover automático, mitigando o custo de parada da linha (estimado em R$ 120.000 por minuto).

| Categoria | Componente | Marca/Modelo | Quantidade (Referência) | Localização/Função | Lógica de Dimensionamento | Disponibilidade no Brasil | Suporte Técnico Local | Certificações |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Identificação | Leitor UHF | SICK RFU620 | 4 unidades | M100, Tacto 123, Tacto 127, G700 | 1 por ponto crítico de identificação | Disponível via distribuidor autorizado (Lead time: 45-60 dias) | SICK Brasil (SP) - Suporte técnico e peças | ANATEL homologado |
| Medição | Sensor de Torque | HBM T10F | 4 por ponto | Montagem rodas (Tacto 123) | 1 sensor por posição de roda (4 rodas) | Importação direta (Lead time: 90-120 dias) | HBM Brasil (SP) - Calibração e manutenção | INMETRO (metrologia legal) |
| Medição | Sensor de Posicionamento | Balluff BTL | 4 por ponto | Montagem rodas (Tacto 123) | 1 sensor por posição de roda (4 rodas) | Estoque local Balluff Brasil (SP) - Lead time: 15-30 dias | Balluff Brasil - Suporte técnico | CE, IP67 |
| Monitoramento | Sensor de Vibração | IFM/VSA | Por máquina | Monitoramento preditivo | 1 por motor/equipamento crítico | Estoque local IFM Brasil (SP) - Lead time: 7-15 dias | IFM Brasil - Suporte técnico e calibração | CE, IP67 |
| Atuação | Chave de Aperto Eletrônica | Atlas Copco Tensor DS | 4 atuadores | Montagem rodas (Tacto 123) | 1 por roda | Estoque local Atlas Copco Brasil (SP) - Lead time: 30-45 dias | Atlas Copco Brasil - Suporte técnico e calibração | CE, ISO 9001 |
| Controle | PLC Siemens S7-1500 | Siemens | 3 unidades | Tacto 123, Supervisão, Redundância | Alta capacidade (32-44 pontos) | Estoque local Siemens Brasil (SP) - Lead time: 30-60 dias | Siemens Brasil - Suporte técnico 24/7 | CE, UL, CSA |
| Controle | PLC Siemens S7-1200 | Siemens | 3 unidades | M100, Tacto 127, G700 | Média capacidade (16-22 pontos) | Estoque local Siemens Brasil (SP) - Lead time: 15-30 dias | Siemens Brasil - Suporte técnico 24/7 | CE, UL, CSA |

**Nota sobre Disponibilidade e Sustentabilidade Comercial:**

&nbsp;&nbsp;&nbsp;&nbsp;Após consulta com stakeholders e fornecedores, identificou-se que:

* **Componentes com Estoque Local (Alta Disponibilidade):** Balluff, IFM e Atlas Copco mantêm estoque no Brasil, reduzindo lead time para 7-45 dias e eliminando risco cambial imediato. Estes componentes representam **60% do volume de sensores** do projeto.
* **Componentes com Distribuidor Autorizado (Média Disponibilidade):** SICK e Siemens possuem distribuidores autorizados no Brasil, com lead time de 30-60 dias. O suporte técnico local garante manutenção preventiva e corretiva sem necessidade de envio ao exterior.
* **Componentes de Importação Direta (Alta Criticidade):** HBM T10F (sensores de torque) são importados diretamente devido à especificidade técnica. Lead time de 90-120 dias exige planejamento antecipado e estoque de segurança de **2 unidades** para garantir continuidade operacional.

#### 1.1.2. Camada de Comunicação (Conectividade e Protocolos)

&nbsp;&nbsp;&nbsp;&nbsp;A Rede Física é *cabeada (TCP/IP)* no caminho de dados crítico (da recepção ao banco de dados) para evitar interferências em ambiente fabril e garantir estabilidade. A integração entre a Tecnologia da Operação (OT) e a Tecnologia da Informação (TI) é realizada através de Gateways e protocolos modernos de alto desempenho.

| Categoria | Componente | Protocolo/Tecnologia | Função | Lógica de Dimensionamento | Disponibilidade no Brasil | Suporte Técnico Local |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Rede Física | Cabo Rede Industrial | TCP/IP Cabeado | Conexão física de dados em tempo real e de baixa latência | 20-30% extra para expansões futuras | Nacional (Prysmian, Furukawa) - Lead time: 7-14 dias | Distribuidores locais |
| Rede Física | Switches Industriais | Ethernet Industrial | Distribuição de rede e redundância (anel) | 1 switch por célula + redundância | Siemens Scalance - Estoque local (Lead time: 15-30 dias) | Siemens Brasil |
| Gateway | Gateway OT/TI | TCP | Interface PLC-Servidor (Segregação de rede) | 1 gateway por grupo de 3-5 CLPs | Siemens IOT2050 - Estoque local (Lead time: 20-40 dias) | Siemens Brasil |
| Protocolo | OPC-UA | OPC Unified Architecture | Comunicação industrial padronizada (S7-1500/1200) | Implementado em PLCs recentes | Nativo nos PLCs Siemens | Suporte via Siemens |
| Protocolo | MQTT | Message Queuing | Comunicação leve e assíncrona com middleware (Node-RED) | Uso para dados de sensores e telemetria | Open Source (Mosquitto) | Suporte via comunidade e integradores |

#### 1.1.3. Camada de Aplicação (TI - Servidor e Dados)

&nbsp;&nbsp;&nbsp;&nbsp;Esta camada exige altíssima performance para processar mais de 50.000 eventos/hora. A escolha por sistemas IBM de missão crítica garante disponibilidade e poder de processamento.

| Categoria | Componente | Tecnologia | Função | Lógica de Dimensionamento | Disponibilidade no Brasil | Suporte Técnico Local |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Servidores | Servidor IBM Master | IBM Power Systems | Ala 22 (primário) - Alta capacidade | Capacidade para 50.000+ eventos/hora | Importação direta IBM Brasil (Lead time: 90-180 dias) | IBM Brasil - Suporte técnico 24/7 |
| Servidores | Servidor IBM Mirror | IBM Power Systems | Ala 13 (secundário) - Espelhamento síncrono | Redundância de hardware (Failover) | Importação direta IBM Brasil (Lead time: 90-180 dias) | IBM Brasil - Suporte técnico 24/7 |
| Alta Disponibilidade | PowerHA Cluster | IBM PowerHA | Failover automático (Cluster 2-nós) | Tempo de recuperação $<500$ms | Licença via IBM Brasil | IBM Brasil - Suporte técnico |
| Banco de Dados | DB2 Database | IBM DB2 | Armazenamento transacional de missão crítica | SSD RAID-10, 6TB estimado | Licença via IBM Brasil | IBM Brasil - Suporte técnico |
| Middleware | Node-RED | JavaScript/Flow | Orquestração IoT e lógica de negócios | 1 instância por servidor + backup | Open Source | Suporte via comunidade e integradores |
| Aplicações | FIS / CobrA System | Sistema legado | Gestão Produção / Controle Qualidade | Integração via APIs REST | Sistemas existentes Volkswagen | Suporte interno Volkswagen |
| Rede | Private Subnet | VLANs segregadas | Segurança de dados e segregação OT/TI | VLANs segregadas por camada | Infraestrutura existente | Suporte interno Volkswagen |

---

### 1.2. Justificativa das Escolhas Técnicas

&nbsp;&nbsp;&nbsp;&nbsp;As escolhas são regidas pela alta criticidade da linha de produção e pelo padrão global da indústria automotiva, **validadas com stakeholders e ajustadas para realidade brasileira**.

| Componente/Categoria | Escolha Técnica | Justificativa | Validação com Stakeholders |
| :--- | :--- | :--- | :--- |
| *CLPs* | Siemens S7-1500/1200 | *Padrão inegociável da Volkswagen*, garante compatibilidade, suporte técnico e conhecimento de base. O S7-1500 é crucial para processamento de alto volume de dados (OPC-UA, MQTT). **Siemens Brasil mantém estoque local e suporte técnico 24/7**, reduzindo risco operacional. | Validado com equipe de Automação Volkswagen - Confirmação de padrão corporativo e disponibilidade de técnicos certificados. |
| *Redundância N+1 (PLCs/Servidores)* | PLCs Espelhados e PowerHA Cluster | *Justificativa Crítica de Negócios:* Proteção contra o custo de parada de R$ 120.000/min. Garante disponibilidade de 99,99% em ambas as pontas (OT e TI) com failover rápido. | Validado com equipe de Produção - Custo de parada confirmado e aceito como justificativa de investimento. |
| *Sensores de Torque* | HBM T10F (Alta Precisão) | Requisito de *qualidade de laboratório* no chão de fábrica. O controle de torque na montagem de rodas é um parâmetro de segurança crítico para evitar recalls. **HBM Brasil oferece calibração local (INMETRO)**, reduzindo custo de manutenção. | Validado com equipe de Qualidade - Especificação técnica confirmada como requisito de segurança. |
| *Sensores com Estoque Local* | Balluff, IFM, Atlas Copco | **Estratégia de Mitigação de Risco:** Componentes com estoque local (60% do volume) garantem reposição rápida (7-45 dias) e reduzem dependência cambial. Suporte técnico local garante manutenção preventiva. | Validado com equipe de Manutenção - Confirmação de experiência positiva com estes fornecedores em outros projetos. |
| *Rede Física* | TCP/IP Cabeado | O ambiente industrial compromete o Wi-Fi. O cabeamento (*caminho crítico de dados OT/TI) garante **estabilidade, baixa latência e consistência* de taxa de transferência, vitais para controle em tempo real. **Cabo nacional reduz custo e lead time**. | Validado com equipe de TI - Confirmação de infraestrutura existente e capacidade de expansão. |
| *Middleware* | Node-RED | Ferramenta low-code e flexível. Atua como orquestrador, permitindo o desenvolvimento rápido de flows para traduzir, processar e rotear dados entre protocolos díspares (MQTT, REST) de forma escalável. **Open Source elimina custo de licenciamento**. | Validado com equipe de Desenvolvimento - Confirmação de expertise interna e redução de dependência de fornecedores externos. |

---

## 2. Precificação da Infraestrutura e Desafios de Custo

### 2.1. Premissas e Metodologia de Cálculo

&nbsp;&nbsp;&nbsp;&nbsp;A metodologia de custo foca no impacto da importação formal (Pessoa Jurídica) no preço final (CAPEX) dos equipamentos. **As premissas foram validadas com equipe de Compras e Financeiro da Volkswagen.**

**Premissas Explícitas:**

* **Câmbio Base:** US$ 1.00 = R$ 5,40 (Data de referência: Novembro/2025 - Fonte: Banco Central do Brasil)
* **Volume por Estação:** 4 sensores de torque por estação (Tacto 123), 4 leitores UHF distribuídos (M100, Tacto 123, Tacto 127, G700)
* **Descontos Corporativos:** 15% de desconto sobre preço FOB para compras em larga escala (validado com fornecedores Siemens, SICK)
* **Carga Tributária Efetiva:** 45% sobre o valor FOB em USD, que é a alíquota média simplificada de incidência em cascata de:
  * Imposto de Importação (II): 16% (NCM específica)
  * IPI: 10-15% (conforme produto)
  * PIS/COFINS-Importação: 9,25%
  * ICMS: 12% (SP)
* **Custo Nacionalizado (BRL):** O valor final de aquisição, após a soma do custo FOB convertido e da tributação (FOB BRL + Tributos BRL)
* **Economia de Escala:** Redução de 20-30% no preço FOB unitário para compras em larga escala (validado com fornecedores)

**Fontes de Preços e Datas:**

* **Siemens:** Cotação oficial Siemens Brasil - (com desconto corporativo estimado da Volkswagen)
* **SICK:** Cotação distribuidor autorizado 
* **HBM:** Cotação HBM Brasil - (importação direta)
* **Balluff, IFM, Atlas Copco:** Cotações fornecedores locais 
* **IBM:** Cotação IBM Brasil - (com desconto corporativo)

### 2.2. Cenário de Produção em Larga Escala (Custos de Importação)

&nbsp;&nbsp;&nbsp;&nbsp;Valores unitários mais baixos (poder de compra por volume). **Preços refletem descontos corporativos e economia de escala.**

#### 2.2.1. Camada de Percepção e Controle

| Componente | Importação (USD) - FOB | Importação (BRL) - FOB* | Carga Tributária Estimada (45% do USD) | *Custo Total Estimado (Nacionalizado)* | Fonte/Data |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Leitor UHF/RFID | US$ 2.290 | R$ 12.366 | US$ 1.030,50 | *R$ 17.931* | SICK Brasil - Jan/2025 |
| Sensor de Torque | US$ 9.000 | R$ 48.600 | US$ 4.050,00 | *R$ 70.470* | HBM Brasil - Jan/2025 |
| Sensor de Posição (linear) | US$ 1.200 | R$ 6.480 | US$ 540,00 | *R$ 9.450* | Balluff Brasil - Jan/2025 |
| Sensor de Vibração | US$ 275 | R$ 1.485 | US$ 123,75 | *R$ 2.162* | IFM Brasil - Jan/2025 |
| Atuador de Aperto (Fixação) | US$ 8.500 | R$ 45.900 | US$ 3.825,00 | *R$ 66.750* | Atlas Copco Brasil - Jan/2025 |
| CLP – CPU S7‑1500 | US$ 3.000 | R$ 16.200 | US$ 1.350,00 | *R$ 23.625* | Siemens Brasil - Jan/2025 |
| CLP – CPU S7‑1200 | US$ 870 | R$ 4.698 | US$ 391,50 | *R$ 6.845* | Siemens Brasil - Jan/2025 |
| Cabo PROFINET/Ethernet (por metro) | US$ 5/m | R$ 27,00/m | US$ 2,25/m | *R$ 40,50/m* | Prysmian Brasil - Jan/2025 |

#### 2.2.2. Camada de Comunicação e Aplicação

&nbsp;&nbsp;&nbsp;&nbsp;Estes itens são utilizados em menor quantidade unitária, mas devido ao alto valor, o impacto tributário é o mesmo.

| Componente | Modelo/Tecnologia (Escolhido) | Importação (USD) - FOB | Carga Tributária Estimada (45% do USD) | *Custo Total Estimado (Nacionalizado)* | Fonte/Data |
| :--- | :--- | :---: | :---: | :---: | :--- |
| *Switch industrial* | Siemens Scalance (Gerenciável) | US$ 483,40 | US$ 217,53 | *R$ 3.785* | Siemens Brasil - Jan/2025 |
| *Gateway OT/TI* | Siemens IOT2050 | US$ 684,70 | US$ 308,12 | *R$ 5.350* | Siemens Brasil - Jan/2025 |
| *DB Reader/OPC Server* | Kepware (Licença base) | US$ 3.240,70 | US$ 1.458,32 | *R$ 25.375* | Kepware Brasil - Jan/2025 |
| *IBM Power – Master* | Power9/Power10 | US$ 114.943 | US$ 51.724 | *R$ 900.000* | IBM Brasil - Jan/2025 |
| *IBM Power – Mirror* | Power9/Power10 | US$ 114.943 | US$ 51.724 | *R$ 900.000* | IBM Brasil - Jan/2025 |
| *PowerHA Cluster (2 nós)* | IBM PowerHA (Licença) | US$ 7.716 | US$ 3.472 | *R$ 55.000* | IBM Brasil - Jan/2025 |
| *IBM DB2 (~6 TB)* | DB2 Enterprise (Licença) | US$ 15.432 | US$ 6.944 | *R$ 110.000* | IBM Brasil - Jan/2025 |
| *Protocolos (OPC-UA/MQTT/REST)* | Nativos / OSS | N/A | N/A | *R$ 0* | Open Source |

### 2.3. Cenário de Produção em Baixa Escala (Custos de Reposição)

&nbsp;&nbsp;&nbsp;&nbsp;A *Regra Principal* para Baixa Escala é: *preço FOB unitário inflacionado* (20% a 30% mais alto) devido à ineficiência volumétrica (compras MRO/reposição de urgência), mas com a *Carga Tributária Efetiva mantida em 45%*.

| Componente | Importação (USD) - FOB | Importação (BRL) - FOB* | Carga Tributária Estimada (45% do USD) | *Custo Total Estimado (Nacionalizado)* |
| :--- | :---: | :---: | :---: | :---: |
| Leitor UHF/RFID | US$ 2.700 | R$ 14.580 | US$ 1.215,00 | *R$ 21.206* |
| Sensor de Torque | US$ 11.500 | R$ 62.100 | US$ 5.175,00 | *R$ 90.038* |
| Sensor de Posição (linear) | US$ 1.850 | R$ 9.990 | US$ 832,50 | *R$ 14.524* |
| Sensor de Vibração | US$ 370 | R$ 1.998 | US$ 166,50 | *R$ 2.910* |
| Atuador de Aperto (Fixação) | US$ 10.500 | R$ 56.700 | US$ 4.725,00 | *R$ 82.358* |
| CLP – CPU S7‑1500 | US$ 3.700 | R$ 19.980 | US$ 1.665,00 | *R$ 29.104* |
| CLP – CPU S7‑1200 | US$ 1.100 | R$ 5.940 | US$ 495,00 | *R$ 8.649* |
| Cabo PROFINET/Ethernet (por metro) | US$ 7/m | R$ 37,80/m | US$ 3,15/m | *R$ 55,10/m* |

### 2.4. Análise de Fluxo de Caixa e Desembolso Mensal

&nbsp;&nbsp;&nbsp;&nbsp;O projeto prevê implementação em **18 meses**, com desembolsos distribuídos conforme lead times e cronograma de instalação. O impacto no capital de giro é crítico devido à necessidade de pagamento antecipado de tributos no desembaraço aduaneiro.

**Cronograma de Desembolso (18 meses):**

| Mês | Componente | Valor (R$) | Justificativa |
| :--- | :--- | :---: | :--- |
| 1-3 | Servidores IBM Power (Master + Mirror) | R$ 1.800.000 | Lead time de 90-180 dias exige pedido antecipado |
| 1-3 | Licenças IBM (PowerHA + DB2) | R$ 165.000 | Licenças adquiridas junto com hardware |
| 4-6 | PLCs Siemens (S7-1500 + S7-1200) | R$ 91.875 | Lead time de 30-60 dias, instalação no mês 6 |
| 4-6 | Sensores HBM (Torque) | R$ 281.880 | Lead time de 90-120 dias, estoque de segurança |
| 7-9 | Sensores Balluff, IFM, Atlas Copco | R$ 312.000 | Estoque local, instalação no mês 9 |
| 7-9 | Leitores SICK UHF | R$ 71.724 | Lead time de 45-60 dias |
| 10-12 | Switches, Gateways, Cabos | R$ 45.000 | Infraestrutura de rede, instalação no mês 12 |
| 13-15 | Integração e Testes | R$ 200.000 | Serviços de integração |
| 16-18 | Comissionamento e Go-Live | R$ 100.000 | Serviços finais |

**Total CAPEX:** R$ 3.067.479

**Impacto no Capital de Giro:**

* **Antecipação de Tributos:** 45% do valor FOB deve ser pago no desembaraço aduaneiro, antes do equipamento entrar em operação
* **Capital Imobilizado:** R$ 1.380.000 (45% de R$ 3.067.479) imobilizado por 3-6 meses antes da operação
* **Custo de Oportunidade:** Considerando taxa de juros de 1,5% ao mês, o custo de oportunidade do capital imobilizado é de **R$ 82.800** (6 meses)

### 2.5. Análise de Sensibilidade de Custos

&nbsp;&nbsp;&nbsp;&nbsp;A análise de sensibilidade avalia o impacto de variações nos principais fatores de custo:

| Fator de Variação | Variação | Impacto no CAPEX Total | Justificativa |
| :--- | :---: | :---: | :--- |
| **Câmbio (USD/BRL)** | +10% (R$ 5,94) | +R$ 306.748 (+10%) | Dependência total de importação |
| **Câmbio (USD/BRL)** | -10% (R$ 4,86) | -R$ 306.748 (-10%) | Redução proporcional |
| **Carga Tributária** | +5% (50% total) | +R$ 153.374 (+5%) | Mudança regulatória |
| **Carga Tributária** | -5% (40% total) | -R$ 153.374 (-5%) | Regime ex-tarifário |
| **Lead Time Extenso** | +30 dias | +R$ 50.000 (custo de oportunidade) | Atraso na entrada em operação |
| **Economia de Escala** | -20% (perda de desconto) | +R$ 613.496 (+20%) | Compra em menor volume |

**Cenário Pessimista (Câmbio +10%, Tributos +5%):** CAPEX = R$ 3.527.601 (+15%)

**Cenário Otimista (Câmbio -10%, Regime Ex-Tarifário):** CAPEX = R$ 2.607.357 (-15%)

### 2.6. Desafios Financeiros e Logísticos da Importação

&nbsp;&nbsp;&nbsp;&nbsp;A dependência de componentes importados de alto valor impõe desafios significativos:

* *Impacto no Fluxo de Caixa (Antecipação de Tributos):* A tributação de *40% a 55%* deve ser paga no desembaraço aduaneiro, exigindo grande capital de giro antes que o equipamento esteja em operação.
* *Risco Cambial:* Qualquer variação na cotação do Dólar (USD) impacta diretamente o custo em Reais do projeto, devido à dependência total de fornecedores globais (Siemens, IBM, HBM).
* **Lead Time Extenso:** O prazo de entrega de 60 a 180 dias para componentes críticos (PLCs, Servidores) exige um planejamento de supply chain rigoroso e a manutenção de um *estoque de segurança* alto, imobilizando mais capital.
* *Mitigação (Ex-Tarifário/Drawback):* A busca por regimes especiais como o **Ex-Tarifário** (redução da alíquota do II de 16% para 0-2%) e **Drawback** (suspensão de tributos para produtos exportados) é uma estratégia *crítica* para viabilizar financeiramente a modernização (Manufatura 4.0). **Validado com equipe de Compras:** A Volkswagen possui processos estabelecidos para solicitação de ex-tarifário junto à CAMEX, com histórico de aprovação em projetos de modernização industrial.

**Certificações Regulatórias Brasileiras:**

* **ANATEL:** Leitores UHF/RFID (SICK RFU620) devem possuir homologação ANATEL para operação em frequências industriais. **Status:** Modelo homologado, processo de importação simplificado.
* **INMETRO:** Sensores de torque (HBM T10F) utilizados em controle de qualidade devem possuir certificação INMETRO para metrologia legal. **Status:** HBM Brasil oferece calibração INMETRO local, reduzindo custo e lead time.
* **CE Marking:** Todos os componentes industriais devem possuir certificação CE para importação. **Status:** Todos os componentes selecionados possuem certificação CE.

---

## 3. Arquitetura no Contexto Administrativo (Gestão e Contrato)

### 3.1. Conceito de Arquitetura como Contrato com Fornecedores

&nbsp;&nbsp;&nbsp;&nbsp;A arquitetura detalhada e padronizada funciona como uma **especificação técnica mandatória**, transformando requisitos de engenharia em cláusulas contratuais inegociáveis e **acordos operacionais mensuráveis**:

* **Padronização:** A especificação de marcas e modelos (**Siemens, SICK, IBM**) garante a compatibilidade e a interoperabilidade com o ecossistema existente da Volkswagen.
* **Contrato de Performance:** A exigência de redundância (N+1, PowerHA) e capacidade (**50.000+ eventos/hora**) vincula legalmente o fornecedor a entregar um sistema que atinja os altos **níveis de disponibilidade** requeridos pela linha de produção.
* **Acordos Operacionais (SLAs):** A arquitetura define **Service Level Agreements (SLAs)** mensuráveis que estabelecem responsabilidades operacionais contínuas, não apenas na entrega inicial, mas na operação sustentável do sistema.

### 3.2. Responsabilidades Definidas dos Fornecedores

&nbsp;&nbsp;&nbsp;&nbsp;A arquitetura estabelece fronteiras claras de responsabilidade (*ownership*), essencial para evitar o "jogo de empurra" em caso de falhas:

| Fornecedor/Parte | Foco de Responsabilidade | Exemplo Prático | SLA/SLO Definido |
| :--- | :--- | :--- | :--- |
| **Volkswagen (TI/OT)** | Definição da Arquitetura, Regras de Negócio e Segurança | Garantir que as **VLANs** estejam seguras e que o **Node-RED** aplique a lógica correta. | Disponibilidade de rede: 99,9% |
| **Integrador de Sistemas (OT)** | **Camada de Percepção e Controle** | Instalação e programação dos CLPs S7-1500, Sensores HBM/Balluff e Atuadores Atlas Copco. | **SLA:** Tempo de resposta para falhas críticas: < 2 horas. **SLO:** Disponibilidade de sensores: 99,5% |
| **Fornecedor de Infraestrutura (TI)** | **Camada de Aplicação** e Alta Disponibilidade | Manutenção dos Servidores IBM Power, Cluster PowerHA e Banco de Dados DB2. | **SLA:** Tempo de resposta para falhas críticas: < 1 hora. **SLO:** Disponibilidade de servidores: 99,99%, MTTR (Mean Time To Repair): < 4 horas |
| **Fornecedores de Software (FIS/CobrA)** | Interface e API | Garantir que as APIs **REST** forneçam a integração de dados bidirecional de forma estável. | **SLA:** Latência p95 de API: < 200ms. **SLO:** Disponibilidade de API: 99,9% |
| **Fornecedores de Componentes (Siemens, SICK, etc.)** | Suporte Técnico e Reposição | Garantir disponibilidade de peças de reposição e suporte técnico. | **SLA:** Lead time de reposição: < 30 dias (estoque local) ou < 90 dias (importação). **SLO:** Tempo de resposta para suporte técnico: < 4 horas (crítico) |

### 3.3. Critérios de Desempenho Mensuráveis (SLOs e SLAs)

&nbsp;&nbsp;&nbsp;&nbsp;A arquitetura define **Service Level Objectives (SLOs)** e **Service Level Agreements (SLAs)** mensuráveis que estabelecem critérios objetivos de desempenho:

| Métrica | SLO (Objetivo) | SLA (Acordo) | Método de Medição | Responsável |
| :--- | :---: | :---: | :--- | :--- |
| **Disponibilidade do Sistema** | 99,99% | 99,95% (com penalidades abaixo) | Monitoramento 24/7 via IBM PowerHA | Fornecedor de Infraestrutura (TI) |
| **Latência p95 (Sensor → BD)** | < 100ms | < 200ms | Monitoramento de rede e aplicação | Fornecedor de Infraestrutura (TI) |
| **Tempo de Recuperação (Failover)** | < 500ms | < 1s | Testes de failover automático | Fornecedor de Infraestrutura (TI) |
| **MTTR (Mean Time To Repair)** | < 2 horas | < 4 horas | Registro de incidentes e tempo de resolução | Integrador de Sistemas (OT) |
| **Disponibilidade de Sensores** | 99,5% | 99,0% | Monitoramento de saúde de sensores | Integrador de Sistemas (OT) |
| **Taxa de Erro de Dados** | < 0,1% | < 0,5% | Validação de integridade de dados | Fornecedor de Infraestrutura (TI) |
| **Tempo de Resposta de Suporte** | < 2 horas (crítico) | < 4 horas (crítico) | Sistema de tickets | Todos os fornecedores |

**Penalidades por Descumprimento de SLA:**

* **Disponibilidade abaixo de 99,95%:** Desconto de 5% na fatura mensal por cada 0,1% abaixo do SLA
* **MTTR acima de 4 horas:** Multa de R$ 10.000 por incidente crítico
* **Latência p95 acima de 200ms:** Desconto de 2% na fatura mensal

### 3.4. Critérios de Viabilidade Operacional

&nbsp;&nbsp;&nbsp;&nbsp;A viabilidade garante que a arquitetura seja sustentável e rentável no longo prazo:

* **TCO (Custo Total de Propriedade):** A escolha por marcas padrão (Siemens, IBM) reduz o TCO, pois há maior disponibilidade de técnicos e peças de reposição no mercado. **Validado com equipe de Manutenção:** Redução estimada de 30% no custo de manutenção comparado a marcas não padronizadas.
* **Manutenibilidade e Disponibilidade:** A padronização de PLCs e o uso da redundância N+1 e PowerHA são críticos para atingir a **disponibilidade de 99,99%**. **SLOs mensuráveis garantem accountability dos fornecedores.**
* **Escalabilidade e Flexibilidade:** O dimensionamento de folga (20-30% extra no cabo) e o uso do Node-RED garantem **flexibilidade** para adicionar novos sensores e linhas sem reescrever o código do CLP ou ERP.
* **Viabilidade Financeira (ROI):** A arquitetura se justifica pelo ROI, visando a **Otimização dos Estoques** e a **Redução de Falhas de Qualidade** (via controle de torque), compensando o alto investimento em CAPEX e tributos. **ROI estimado em 3,5 anos** (validado com equipe Financeira).

---

## 4. Diagrama da Arquitetura

### 4.1. Diagrama Visual Desenvolvido no draw.io

<div align="center">
<sub>Figura - Arquitetura IoT Refinada</sub>
</div>
<div align="center">
<img src="../../assets/Diagrama sem nome.drawio.svg">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025</sub>
</div>

**Legenda do Diagrama:**

* **Protocolos e Direção de Fluxo:**
  * OPC-UA (seta azul): Comunicação PLC → Gateway (bidirecional)
  * MQTT (seta verde): Comunicação Gateway → Middleware (publish/subscribe)
  * REST (seta laranja): Comunicação Middleware → Sistemas Legados (request/response)
  * TCP/IP (linha preta): Rede física cabeada

* **Notas de Segurança (ACL):**
  * VLANs segregadas: OT (VLAN 100), TI (VLAN 200), DMZ (VLAN 300)
  * Firewall entre camadas OT e TI
  * Autenticação MQTT via certificados X.509

* **Componentes com Estoque Local (marcados com *):**
  * Balluff, IFM, Atlas Copco (estoque local - lead time reduzido)

---

## 5. Benefícios Operacionais

### 5.1. Continuidade Operacional e Redução de Riscos (Disponibilidade)

&nbsp;&nbsp;&nbsp;&nbsp;Benefícios **mensuráveis e validados com stakeholders**:

| Benefício Operacional | Mecanismo Arquitetural | Impacto Mensurável na Linha de Produção | Validação com Stakeholders |
| :--- | :--- | :--- | :--- |
| **Proteção Contra Paradas** | **Redundância N+1** (PLCs S7-1500) e **Cluster PowerHA** (Servidores IBM) | Redução de **95% no risco de parada não programada** (de 4 eventos/ano para 0,2 eventos/ano). Economia estimada: **R$ 4.800.000/ano** (evitar 40 minutos de parada/ano). | Validado com equipe de Produção - Confirmação de custo de parada e aceitação de meta de redução. |
| **Tempo de Recuperação Mínimo** | *Failover* Automático (< 500ms) | **Zero impacto** na produção em caso de falha de hardware primário. Disponibilidade de **99,99%** (4,38 minutos de downtime/ano). | Validado com equipe de TI - Confirmação de capacidade técnica do PowerHA. |
| **Estabilidade da Rede** | **Rede Física Cabeada (TCP/IP)** e Switches Industriais | Redução de **80% em falhas de comunicação** comparado a Wi-Fi (de 10 eventos/mês para 2 eventos/mês). | Validado com equipe de Automação - Experiência em outros projetos confirma superioridade do cabeamento. |

### 5.2. Otimização de Qualidade e Rastreabilidade (Controle e Conformidade)

| Benefício Operacional | Mecanismo Arquitetural | Impacto Mensurável na Linha de Produção | Validação com Stakeholders |
| :--- | :--- | :--- | :--- |
| **Zero Defeitos Críticos** | **Sensores HBM T10F** (Alta Precisão) e Atuadores Atlas Copco | Redução de **90% em defeitos de torque** (de 0,1% para 0,01% de veículos). **Eliminação de recalls por falha de torque** (economia estimada: R$ 50.000.000/ano em recall evitado). | Validado com equipe de Qualidade - Confirmação de especificação técnica e histórico de recalls. |
| **Rastreabilidade Unívoca** | **Leitores SICK UHF/QR Code** (M100, Tacto 123/127, G700) | **100% de rastreabilidade** de componentes (roda, banco) e parâmetros de qualidade (torque) associados ao VIN. Redução de **70% no tempo de investigação de problemas de campo** (de 2 semanas para 3 dias). | Validado com equipe de Qualidade - Confirmação de necessidade de rastreabilidade para auditoria. |
| **Integração de Qualidade** | **Sistemas CobrA (via REST API)** | **Tempo real** de integração de dados de qualidade (latência < 200ms). Redução de **50% no tempo de validação de conformidade** (de 4 horas para 2 horas por lote). | Validado com equipe de Qualidade - Confirmação de necessidade de integração em tempo real. |

### 5.3. Eficiência e Sustentabilidade (Manutenção Preditiva e Flexibilidade)

| Benefício Operacional | Mecanismo Arquitetural | Impacto Mensurável na Linha de Produção | Validação com Stakeholders |
| :--- | :--- | :--- | :--- |
| **Redução de Manutenção Corretiva** | **Sensores de Vibração/Temperatura (IFM)** | Redução de **60% em manutenção corretiva** (de 12 eventos/ano para 5 eventos/ano). Conversão de **80% das paradas não programadas em paradas programadas**. Economia estimada: **R$ 1.200.000/ano** (redução de 10 horas de parada/ano). | Validado com equipe de Manutenção - Confirmação de experiência positiva com manutenção preditiva em outros projetos. |
| **Agilidade e Integração de Dados** | **Middleware Node-RED** | Redução de **70% no tempo de desenvolvimento** para adicionar novos sensores (de 3 semanas para 1 semana). **Zero necessidade de reprogramação de CLPs** para mudanças de lógica de negócios. | Validado com equipe de Desenvolvimento - Confirmação de expertise interna e redução de dependência de fornecedores externos. |
| **Redução de Capital de Giro** | **Componentes com Estoque Local (60% do volume)** | Redução de **40% no lead time médio** de reposição (de 90 dias para 30 dias). Redução de **R$ 500.000 em estoque de segurança** necessário. | Validado com equipe de Compras - Confirmação de disponibilidade de estoque local e redução de risco cambial. |

### 5.4. Resumo Executivo de Benefícios Mensuráveis

| Categoria de Benefício | Impacto Quantitativo | Valor Estimado (R$/ano) |
| :--- | :--- | :--- |
| **Redução de Paradas Não Programadas** | 95% de redução (40 minutos/ano evitados) | R$ 4.800.000 |
| **Eliminação de Recalls por Falha de Torque** | 100% de eliminação | R$ 50.000.000 |
| **Redução de Manutenção Corretiva** | 60% de redução (10 horas/ano evitadas) | R$ 1.200.000 |
| **Redução de Capital de Giro (Estoque)** | R$ 500.000 em estoque reduzido | R$ 75.000 (custo de oportunidade) |
| **Redução de Tempo de Investigação de Qualidade** | 70% de redução (economia de 11 semanas/ano) | R$ 550.000 |
| **TOTAL DE BENEFÍCIOS OPERACIONAIS** | | **R$ 56.625.000/ano** |

**ROI do Projeto:** CAPEX de R$ 3.067.479 com benefícios anuais de R$ 56.625.000 resulta em **ROI de 1.745%** e **payback de 0,05 anos (18 dias)**.

---

## 6. Referências e Fontes de Dados

### 6.1. Fontes de Cotações e Preços de Componentes

#### 6.1.1. Fornecedores de Componentes Industriais

| Fornecedor | Componente | Tipo de Cotação | Data | Contato/Referência | Observações |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Siemens Brasil** | PLCs S7-1500/1200, Switches Scalance, Gateway IOT2050 | Cotação oficial corporativa | 15/01/2025 | Siemens Brasil - Setor Automação Industrial | Desconto corporativo Volkswagen aplicado (15% sobre FOB) |
| **SICK Brasil** | Leitores UHF RFU620 | Cotação distribuidor autorizado | 18/01/2025 | SICK Brasil - Distribuidor Autorizado SP | Lead time: 45-60 dias, estoque local limitado |
| **HBM Brasil** | Sensores de Torque T10F | Cotação importação direta | 20/01/2025 | HBM Brasil - Representante Oficial | Importação direta, calibração INMETRO disponível localmente |
| **Balluff Brasil** | Sensores de Posicionamento BTL | Cotação fornecedor local | 12/01/2025 | Balluff Brasil - Filial São Paulo | Estoque local, lead time reduzido (15-30 dias) |
| **IFM Brasil** | Sensores de Vibração VSA | Cotação fornecedor local | 14/01/2025 | IFM Brasil - Filial São Paulo | Estoque local, suporte técnico local |
| **Atlas Copco Brasil** | Chaves de Aperto Tensor DS | Cotação fornecedor local | 16/01/2025 | Atlas Copco Brasil - Filial São Paulo | Estoque local, calibração disponível |
| **Prysmian Brasil** | Cabos PROFINET/Ethernet | Cotação fornecedor nacional | 10/01/2025 | Prysmian Brasil - Distribuidor | Produção nacional, sem impacto cambial |
| **IBM Brasil** | Servidores Power Systems, PowerHA, DB2 | Cotação oficial corporativa | 22/01/2025 | IBM Brasil - Setor Enterprise | Desconto corporativo Volkswagen aplicado, lead time: 90-180 dias |
| **Kepware Brasil** | OPC Server (Licença) | Cotação licenciamento | 19/01/2025 | Kepware Brasil - Distribuidor Autorizado | Licenciamento por pontos |

#### 6.1.2. Fontes de Informação de Mercado e Disponibilidade

* **Consulta com Equipe de Compras Volkswagen:** Validação de processos de compra, descontos corporativos e lead times históricos.
* **Consulta com Equipe de Manutenção Volkswagen:** Validação de experiência com fornecedores e disponibilidade de peças de reposição. 

### 6.2. Fontes de Regulamentação Tributária e Aduaneira

#### 6.2.1. Impostos de Importação e Tributação

| Imposto/Tributo | Alíquota Aplicada | Base Legal | Fonte | Data de Consulta |
| :--- | :---: | :--- | :--- | :--- |
| **Imposto de Importação (II)** | 16% (média para equipamentos industriais) | Decreto 6.759/2009 - TEC (Tarifa Externa Comum) | Receita Federal do Brasil | Novembro/2025 |
| **IPI (Imposto sobre Produtos Industrializados)** | 10-15% (conforme NCM específica) | Lei 4.502/1964 e Decreto-Lei 7.212/2010 | Receita Federal do Brasil | Novembro/2025  |
| **PIS/COFINS-Importação** | 9,25% (total) | Lei 10.865/2004 e Lei 10.833/2003 | Receita Federal do Brasil | Novembro/2025 |
| **ICMS (São Paulo)** | 12% | Convênio ICMS 52/2017 | Secretaria da Fazenda de São Paulo | Novembro/2025 |
| **Carga Tributária Efetiva Total** | 45% (média simplificada) | Cálculo em cascata dos tributos acima | Metodologia própria baseada em legislação vigente | Novembro/2025 |

#### 6.2.2. Regimes Especiais de Importação

| Regime Especial | Descrição | Base Legal | Órgão Responsável | Fonte de Consulta |
| :--- | :--- | :--- | :--- | :--- |
| **Ex-Tarifário** | Redução/suspensão da alíquota do II para bens de capital | Resolução CAMEX 13/2012 e Resolução CAMEX 16/2016 | CAMEX (Câmara de Comércio Exterior) | Consulta com Equipe de Compras Volkswagen - Janeiro/2025 |
| **Drawback Suspensivo** | Suspensão de tributos para produtos destinados à exportação | Lei 11.945/2009 e Instrução Normativa RFB 1.911/2019 | Receita Federal do Brasil | Instrução Normativa RFB 1.911/2019 |
| **Repetro** | Regime aduaneiro especial para petróleo e gás (não aplicável) | Lei 9.478/1997 | Receita Federal do Brasil | Não aplicável ao projeto |

**Fontes Legais Específicas:**
* **CAMEX Resolução 13/2012:** Estabelece critérios para concessão de ex-tarifário para bens de capital
* **CAMEX Resolução 16/2016:** Atualiza procedimentos para solicitação de ex-tarifário
* **Instrução Normativa RFB 1.911/2019:** Regulamenta o drawback suspensivo
* **Decreto 6.759/2009:** Aprova a TEC (Tarifa Externa Comum) do Mercosul
* **Lei 10.865/2004:** Institui a Contribuição para o PIS-Importação
* **Lei 10.833/2003:** Institui a Contribuição para o COFINS-Importação
* **Convênio ICMS 52/2017:** Estabelece alíquotas de ICMS para importação

#### 6.2.3. Fontes de Câmbio e Indicadores Econômicos

| Indicador | Valor Utilizado | Fonte | Data de Referência | Observações |
| :--- | :---: | :--- | :--- | :--- |
| **Taxa de Câmbio USD/BRL** | R$ 5,40 | Banco Central do Brasil (BACEN) | 15/01/2025 | Taxa de câmbio comercial (venda) |
| **Taxa de Juros (SELIC)** | 1,5% ao mês (aproximado) | Banco Central do Brasil (BACEN) | Média 2025 | Utilizada para cálculo de custo de oportunidade |
| **IPCA (Inflação)** | Considerado no cálculo de variação de preços | IBGE | Janeiro/2025 | Base para análise de sensibilidade |


### 6.3. Fontes de Regulamentação Técnica e Certificações

#### 6.3.1. Certificações Obrigatórias no Brasil

| Certificação | Componente Aplicável | Base Legal | Órgão Responsável | Fonte |
| :--- | :--- | :--- | :--- | :--- |
| **ANATEL** | Leitores UHF/RFID (SICK RFU620) | Resolução ANATEL 680/2017 | ANATEL (Agência Nacional de Telecomunicações) | Resolução ANATEL 680/2017 - Homologação de equipamentos de radiofrequência |
| **INMETRO** | Sensores de Torque (HBM T10F) | Portaria INMETRO 236/2020 | INMETRO (Instituto Nacional de Metrologia, Qualidade e Tecnologia) | Portaria INMETRO 236/2020 - Metrologia legal para instrumentos de medição |
| **CE Marking** | Todos os componentes industriais | Diretiva CE 2014/35/UE | União Europeia (obrigatório para importação) | Diretiva CE 2014/35/UE - Equipamentos elétricos de baixa tensão |

**Fontes Legais Específicas:**
* **Resolução ANATEL 680/2017:** Estabelece requisitos para homologação de equipamentos de radiofrequência
* **Portaria INMETRO 236/2020:** Regulamenta metrologia legal para instrumentos de medição utilizados em controle de qualidade
* **Diretiva CE 2014/35/UE:** Estabelece requisitos de segurança para equipamentos elétricos (obrigatório para importação da UE)

### 6.4. Validações com Stakeholders Internos

| Stakeholder | Área de Responsabilidade | Tipo de Validação | Data | Observações |
| :--- | :--- | :--- | :--- | :--- |
| **Equipe de Automação Volkswagen** | Padronização técnica e suporte | Validação de padrão corporativo Siemens e disponibilidade de técnicos certificados | 2025 | Confirmação de padrão inegociável e expertise interna |
| **Equipe de Produção** | Operação e continuidade | Confirmação de custo de parada (R$ 120.000/min) e aceitação de meta de redução | 2025 | Validação de criticidade e justificativa de investimento |
| **Equipe de Qualidade** | Conformidade e rastreabilidade | Confirmação de especificação técnica de sensores e necessidade de rastreabilidade | 2025 | Validação de requisitos de qualidade e segurança |
| **Equipe de Manutenção** | Sustentabilidade operacional | Confirmação de experiência positiva com fornecedores e redução de custo de manutenção | 2025 | Validação de TCO e manutenibilidade |
| **Equipe de Compras** | Aquisição e logística | Confirmação de processos de ex-tarifário e disponibilidade de estoque local | 2025 | Validação de viabilidade de compra e lead times |
| **Equipe de TI** | Infraestrutura e disponibilidade | Confirmação de capacidade técnica do PowerHA e infraestrutura existente | 2025 | Validação de arquitetura de alta disponibilidade |
| **Equipe Financeira** | Viabilidade econômica | Validação de ROI e payback estimados | 2025 | Validação de análise financeira e impacto no capital de giro |

### 6.5. Referências Bibliográficas e Documentação Técnica

* **Siemens:** Documentação técnica S7-1500/1200 - Manual de Sistema, 2024 (https://cache.industry.siemens.com/dl/files/115/82212115/att_108330/v2/82212115_s7_communication_s7-1500_en.pdf)

* **SICK:** Documentação técnica RFU620 - Manual do Usuário, 2024
https://www.sick.com/media/docs/2/92/492/operating_instructions_rfu62x_pt_im0056492.pdf

* **HBM:** Documentação técnica T10F - Especificações Técnicas, 2024
https://www.hbm.com/pt/2379/t10f-medidor-de-torque-com-design-extremamente-baixo/

* **IBM:** Documentação técnica PowerHA - Guia de Alta Disponibilidade, 2024
https://www.ibm.com/docs/pt/i/7.4.0?topic=availability-implementing-high

* **Node-RED:** Documentação oficial - https://nodered.org/docs/ - Acesso em Dez/25

