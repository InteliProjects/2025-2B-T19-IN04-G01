## 1. Definição da Arquitetura, Componentes e Funcionalidades

### 1.1. Descrição dos Componentes Principais (Camadas)

#### 1.1.1. Camada de Percepção e Controle (OT - Chão de Fábrica)

&nbsp;&nbsp;&nbsp;&nbsp;A base da arquitetura no chão de fábrica é composta por sensores de identificação, medição e Controladores Lógicos Programáveis (CLPs). A arquitetura é robusta, focada na inspeção, rastreabilidade e no controle de qualidade da montagem de rodas (Tacto 123) e bancos (Tacto 127).

&nbsp;&nbsp;&nbsp;&nbsp;O controle e a consolidação dos dados dos sensores são feitos pelos CLPs. A marca *Siemens (Simatic)* é o padrão inegociável, utilizando-se modelos modernos como o *S7-1200/1500. Para pontos críticos (Tacto 123), o sistema emprega **PLCs redundantes em configuração N+1* para garantir failover automático, mitigando o custo de parada da linha (estimado em R$ 120.000 por minuto).

| Categoria | Componente | Marca/Modelo | Quantidade (Referência) | Localização/Função | Lógica de Dimensionamento |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Identificação | Leitor UHF | SICK RFU620 | 4 unidades | M100, Tacto 123, Tacto 127, G700 | 1 por ponto crítico de identificação |
| Medição | Sensor de Torque | HBM T10F | 4 por ponto | Montagem rodas (Tacto 123) | 1 sensor por posição de roda (4 rodas) |
| Medição | Sensor de Posicionamento | Balluff BTL | 4 por ponto | Montagem rodas (Tacto 123) | 1 sensor por posição de roda (4 rodas) |
| Monitoramento | Sensor de Vibração | IFM/VSA | Por máquina | Monitoramento preditivo | 1 por motor/equipamento crítico |
| Atuação | Chave de Aperto Eletrônica | Atlas Copco Tensor DS | 4 atuadores | Montagem rodas (Tacto 123) | 1 por roda |
| Controle | PLC Siemens S7-1500 | Siemens | 3 unidades | Tacto 123, Supervisão, Redundância | Alta capacidade (32-44 pontos) |
| Controle | PLC Siemens S7-1200 | Siemens | 3 unidades | M100, Tacto 127, G700 | Média capacidade (16-22 pontos) |

#### 1.1.2. Camada de Comunicação (Conectividade e Protocolos)

&nbsp;&nbsp;&nbsp;&nbsp;A Rede Física é *cabeada (TCP/IP)* no caminho de dados crítico (da recepção ao banco de dados) para evitar interferências em ambiente fabril e garantir estabilidade. A integração entre a Tecnologia da Operação (OT) e a Tecnologia da Informação (TI) é realizada através de Gateways e protocolos modernos de alto desempenho.

| Categoria | Componente | Protocolo/Tecnologia | Função | Lógica de Dimensionamento |
| :--- | :--- | :--- | :--- | :--- |
| Rede Física | Cabo Rede Industrial | TCP/IP Cabeado | Conexão física de dados em tempo real e de baixa latência | 20-30% extra para expansões futuras |
| Rede Física | Switches Industriais | Ethernet Industrial | Distribuição de rede e redundância (anel) | 1 switch por célula + redundância |
| Gateway | Gateway OT/TI | TCP | Interface PLC-Servidor (Segregação de rede) | 1 gateway por grupo de 3-5 CLPs |
| Protocolo | OPC-UA | OPC Unified Architecture | Comunicação industrial padronizada (S7-1500/1200) | Implementado em PLCs recentes |
| Protocolo | MQTT | Message Queuing | Comunicação leve e assíncrona com middleware (Node-RED) | Uso para dados de sensores e telemetria |

#### 1.1.3. Camada de Aplicação (TI - Servidor e Dados)

&nbsp;&nbsp;&nbsp;&nbsp;Esta camada exige altíssima performance para processar mais de 50.000 eventos/hora. A escolha por sistemas IBM de missão crítica garante disponibilidade e poder de processamento.

| Categoria | Componente | Tecnologia | Função | Lógica de Dimensionamento |
| :--- | :--- | :--- | :--- | :--- |
| Servidores | Servidor IBM Master | IBM Power Systems | Ala 22 (primário) - Alta capacidade | Capacidade para 50.000+ eventos/hora |
| Servidores | Servidor IBM Mirror | IBM Power Systems | Ala 13 (secundário) - Espelhamento síncrono | Redundância de hardware (Failover) |
| Alta Disponibilidade | PowerHA Cluster | IBM PowerHA | Failover automático (Cluster 2-nós) | Tempo de recuperação $<500$ms |
| Banco de Dados | DB2 Database | IBM DB2 | Armazenamento transacional de missão crítica | SSD RAID-10, 6TB estimado |
| Middleware | Node-RED | JavaScript/Flow | Orquestração IoT e lógica de negócios | 1 instância por servidor + backup |
| Aplicações | FIS / CobrA System | Sistema legado | Gestão Produção / Controle Qualidade | Integração via APIs REST |
| Rede | Private Subnet | VLANs segregadas | Segurança de dados e segregação OT/TI | VLANs segregadas por camada |

---

### 1.2. Justificativa das Escolhas Técnicas

&nbsp;&nbsp;&nbsp;&nbsp;As escolhas são regidas pela alta criticidade da linha de produção e pelo padrão global da indústria automotiva.

| Componente/Categoria | Escolha Técnica | Justificativa |
| :--- | :--- | :--- |
| *CLPs* | Siemens S7-1500/1200 | *Padrão inegociável da Volkswagen*, garante compatibilidade, suporte técnico e conhecimento de base. O S7-1500 é crucial para processamento de alto volume de dados (OPC-UA, MQTT). |
| *Redundância N+1 (PLCs/Servidores)* | PLCs Espelhados e PowerHA Cluster | *Justificativa Crítica de Negócios:* Proteção contra o custo de parada de R$ 120.000/min. Garante disponibilidade de 99,99% em ambas as pontas (OT e TI) com failover rápido. |
| *Sensores de Torque* | HBM T10F (Alta Precisão) | Requisito de *qualidade de laboratório* no chão de fábrica. O controle de torque na montagem de rodas é um parâmetro de segurança crítico para evitar recalls. |
| *Rede Física* | TCP/IP Cabeado | O ambiente industrial compromete o Wi-Fi. O cabeamento (*caminho crítico de dados OT/TI) garante **estabilidade, baixa latência e consistência* de taxa de transferência, vitais para controle em tempo real. |
| *Middleware* | Node-RED | Ferramenta low-code e flexível. Atua como orquestrador, permitindo o desenvolvimento rápido de flows para traduzir, processar e rotear dados entre protocolos díspares (MQTT, REST) de forma escalável. |

---

## 2. Precificação da Infraestrutura e Desafios de Custo

### 2.1. Premissas e Metodologia de Cálculo

&nbsp;&nbsp;&nbsp;&nbsp;A metodologia de custo foca no impacto da importação formal (Pessoa Jurídica) no preço final (CAPEX) dos equipamentos.

* *Câmbio:* US$ 1.00 = R$ 5,40.
* *Carga Tributária Efetiva:* 45% sobre o valor FOB em USD, que é a alíquota média simplificada de incidência em cascata de II, IPI, PIS/COFINS-Importação e ICMS.
* *Custo Nacionalizado (BRL):* O valor final de aquisição, após a soma do custo FOB convertido e da tributação (FOB BRL + Tributos BRL).

### 2.2. Cenário de Produção em Larga Escala (Custos de Importação)

&nbsp;&nbsp;&nbsp;&nbsp;Valores unitários mais baixos (poder de compra por volume).

#### 2.2.1. Camada de Percepção e Controle

| Componente | Importação (USD) - FOB | Importação (BRL) - FOB\* | Carga Tributária Estimada (45% do USD) | *Custo Total Estimado (Nacionalizado)* |
| :--- | :---: | :---: | :---: | :---: |
| Leitor UHF/RFID | US$ 2.290 | R$ 12.366 | US$ 1.030,50 | *R$ 17.931* |
| Sensor de Torque | US$ 9.000 | R$ 48.600 | US$ 4.050,00 | *R$ 70.470* |
| Sensor de Posição (linear) | US$ 1.200 | R$ 6.480 | US$ 540,00 | *R$ 9.450* |
| Sensor de Vibração | US$ 275 | R$ 1.485 | US$ 123,75 | *R$ 2.162* |
| Atuador de Aperto (Fixação) | US$ 8.500 | R$ 45.900 | US$ 3.825,00 | *R$ 66.750* |
| CLP – CPU S7‑1500 | US$ 3.000 | R$ 16.200 | US$ 1.350,00 | *R$ 23.625* |
| CLP – CPU S7‑1200 | US$ 870 | R$ 4.698 | US$ 391,50 | *R$ 6.845* |
| Cabo PROFINET/Ethernet (por metro) | US$ 5/m | R$ 27,00/m | US$ 2,25/m | *R$ 40,50/m* |

#### 2.2.2. Camada de Comunicação e Aplicação

&nbsp;&nbsp;&nbsp;&nbsp;Estes itens são utilizados em menor quantidade unitária, mas devido ao alto valor, o impacto tributário é o mesmo.

| Componente | Modelo/Tecnologia (Escolhido) | Importação (USD) - FOB | Carga Tributária Estimada (45% do USD) | *Custo Total Estimado (Nacionalizado)* |
| :--- | :--- | :---: | :---: | :---: |
| *Switch industrial* | Siemens Scalance (Gerenciável) | US$ 483,40 | US$ 217,53 | *R$ 3.785* |
| *Gateway OT/TI* | Siemens IOT2050 | US$ 684,70 | US$ 308,12 | *R$ 5.350* |
| *DB Reader/OPC Server* | Kepware (Licença base) | US$ 3.240,70 | US$ 1.458,32 | *R$ 25.375* |
| *IBM Power – Master* | Power9/Power10 | US$ 114.943 | US$ 51.724 | *R$ 900.000* |
| *IBM Power – Mirror* | Power9/Power10 | US$ 114.943 | US$ 51.724 | *R$ 900.000* |
| *PowerHA Cluster (2 nós)* | IBM PowerHA (Licença) | US$ 7.716 | US$ 3.472 | *R$ 55.000* |
| *IBM DB2 (~6 TB)* | DB2 Enterprise (Licença) | US$ 15.432 | US$ 6.944 | *R$ 110.000* |
| *Protocolos (OPC-UA/MQTT/REST)* | Nativos / OSS | N/A | N/A | *R$ 0* |

### 2.3. Cenário de Produção em Baixa Escala (Custos de Reposição)

&nbsp;&nbsp;&nbsp;&nbsp;A *Regra Principal* para Baixa Escala é: *preço FOB unitário inflacionado* (20% a 30% mais alto) devido à ineficiência volumétrica (compras MRO/reposição de urgência), mas com a *Carga Tributária Efetiva mantida em 45%*.

| Componente | Importação (USD) - FOB | Importação (BRL) - FOB\* | Carga Tributária Estimada (45% do USD) | *Custo Total Estimado (Nacionalizado)* |
| :--- | :---: | :---: | :---: | :---: |
| Leitor UHF/RFID | US$ 2.700 | R$ 14.580 | US$ 1.215,00 | *R$ 21.206* |
| Sensor de Torque | US$ 11.500 | R$ 62.100 | US$ 5.175,00 | *R$ 90.038* |
| Sensor de Posição (linear) | US$ 1.850 | R$ 9.990 | US$ 832,50 | *R$ 14.524* |
| Sensor de Vibração | US$ 370 | R$ 1.998 | US$ 166,50 | *R$ 2.910* |
| Atuador de Aperto (Fixação) | US$ 10.500 | R$ 56.700 | US$ 4.725,00 | *R$ 82.358* |
| CLP – CPU S7‑1500 | US$ 3.700 | R$ 19.980 | US$ 1.665,00 | *R$ 29.104* |
| CLP – CPU S7‑1200 | US$ 1.100 | R$ 5.940 | US$ 495,00 | *R$ 8.649* |
| Cabo PROFINET/Ethernet (por metro) | US$ 7/m | R$ 37,80/m | US$ 3,15/m | *R$ 55,10/m* |

### 2.4. Desafios Financeiros e Logísticos da Importação

&nbsp;&nbsp;&nbsp;&nbsp;A dependência de componentes importados de alto valor impõe desafios significativos:

* *Impacto no Fluxo de Caixa (Antecipação de Tributos):* A tributação de *40% a 55%* deve ser paga no desembaraço aduaneiro, exigindo grande capital de giro antes que o equipamento esteja em operação.
* *Risco Cambial:* Qualquer variação na cotação do Dólar (USD) impacta diretamente o custo em Reais do projeto, devido à dependência total de fornecedores globais (Siemens, IBM, HBM).
* **Lead Time Extenso:** O prazo de entrega de 60 a 180 dias para componentes críticos (PLCs, Servidores) exige um planejamento de supply chain rigoroso e a manutenção de um *estoque de segurança* alto, imobilizando mais capital.
* *Mitigação (Ex-Tarifário):* A busca por regimes especiais como o Ex-Tarifário (redução da alíquota do II) é uma estratégia *crítica* para viabilizar financeiramente a modernização (Manufatura 4.0), embora a burocracia e os demais tributos persistam.

---

## 3. Arquitetura no Contexto Administrativo (Gestão e Contrato)

### 3.1. Conceito de Arquitetura como Contrato com Fornecedores

&nbsp;&nbsp;&nbsp;&nbsp;A arquitetura detalhada e padronizada funciona como uma **especificação técnica mandatória**, transformando requisitos de engenharia em cláusulas contratuais inegociáveis:

* **Padronização:** A especificação de marcas e modelos (**Siemens, SICK, IBM**) garante a compatibilidade e a interoperabilidade com o ecossistema existente da Volkswagen.
* **Contrato de Performance:** A exigência de redundância (N+1, PowerHA) e capacidade (**50.000+ eventos/hora**) vincula legalmente o fornecedor a entregar um sistema que atinja os altos **níveis de disponibilidade** requeridos pela linha de produção.

### 3.2. Responsabilidades Definidas dos Fornecedores

&nbsp;&nbsp;&nbsp;&nbsp;A arquitetura estabelece fronteiras claras de responsabilidade (*ownership*), essencial para evitar o "jogo de empurra" em caso de falhas:

| Fornecedor/Parte | Foco de Responsabilidade | Exemplo Prático |
| :--- | :--- | :--- |
| **Volkswagen (TI/OT)** | Definição da Arquitetura, Regras de Negócio e Segurança | Garantir que as **VLANs** estejam seguras e que o **Node-RED** aplique a lógica correta. |
| **Integrador de Sistemas (OT)** | **Camada de Percepção e Controle** | Instalação e programação dos CLPs S7-1500, Sensores HBM/Balluff e Atuadores Atlas Copco. |
| **Fornecedor de Infraestrutura (TI)** | **Camada de Aplicação** e Alta Disponibilidade | Manutenção dos Servidores IBM Power, Cluster PowerHA e Banco de Dados DB2. |
| **Fornecedores de Software (FIS/CobrA)** | Interface e API | Garantir que as APIs **REST** forneçam a integração de dados bidirecional de forma estável. |

### 3.3. Critérios de Viabilidade Operacional

&nbsp;&nbsp;&nbsp;&nbsp;A viabilidade garante que a arquitetura seja sustentável e rentável no longo prazo:

* **TCO (Custo Total de Propriedade):** A escolha por marcas padrão (Siemens, IBM) reduz o TCO, pois há maior disponibilidade de técnicos e peças de reposição no mercado.
* **Manutenibilidade e Disponibilidade:** A padronização de PLCs e o uso da redundância N+1 e PowerHA são críticos para atingir a **disponibilidade de 99,99%**.
* **Escalabilidade e Flexibilidade:** O dimensionamento de folga (20-30% extra no cabo) e o uso do Node-RED garantem **flexibilidade** para adicionar novos sensores e linhas sem reescrever o código do CLP ou ERP.
* **Viabilidade Financeira (ROI):** A arquitetura se justifica pelo ROI, visando a **Otimização dos Estoques** e a **Redução de Falhas de Qualidade** (via controle de torque), compensando o alto investimento em CAPEX e tributos.

---

## 4. Diagrama da Arquitetura

### 4.1. Diagrama Visual Desenvolvido no draw.io

<div align="center">
<sub>Figura - Arquitetura IoT</sub>
</div>
<div align="center">
<img src="../../assets/Diagrama sem nome.drawio.svg">
</div>
<div align="center">
<sub>Source: Material produzido pelo Time Sem Parar, 2025.</sub>
</div>


## 5. Benefícios Operacionais

### 5.1. Continuidade Operacional e Redução de Riscos (Disponibilidade)

| Benefício Operacional | Mecanismo Arquitetural | Impacto na Linha de Produção |
| :--- | :--- | :--- |
| **Proteção Contra Paradas** | **Redundância N+1** (PLCs S7-1500) e **Cluster PowerHA** (Servidores IBM) | Mitiga o risco de falha em *qualquer* camada (OT ou TI). Essencial para evitar o custo de **R$ 120.000 por minuto** de parada, garantindo a continuidade do fluxo de produção. |
| **Tempo de Recuperação Mínimo** | *Failover* Automático (< 500ms) | Garante que uma falha de hardware primário seja transparente para o ciclo de produção, mantendo a disponibilidade exigida de **99,99%** para sistemas críticos. |
| **Estabilidade da Rede** | **Rede Física Cabeada (TCP/IP)** e Switches Industriais | Garante a **confiabilidade** da comunicação em tempo real no caminho crítico (sensores ao BD), eliminando a instabilidade do Wi-Fi em ambiente fabril. |

### 5.2. Otimização de Qualidade e Rastreabilidade (Controle e Conformidade)

| Benefício Operacional | Mecanismo Arquitetural | Impacto na Linha de Produção |
| :--- | :--- | :--- |
| **Zero Defeitos Críticos** | **Sensores HBM T10F** (Alta Precisão) e Atuadores Atlas Copco | Assegura que o torque de aperto das rodas atinja precisamente o **parâmetro de segurança** (qualidade laboratorial no chão de fábrica), minimizando drasticamente o risco de *recall* por falha de segurança. |
| **Rastreabilidade Unívoca** | **Leitores SICK UHF/QR Code** (M100, Tacto 123/127, G700) | Associa cada componente (roda, banco) e cada parâmetro de qualidade (torque) ao **número de chassi** (VIN) do veículo. Fundamental para auditoria, controle de conformidade e resposta rápida a problemas de campo. |
| **Integração de Qualidade** | **Sistemas CobrA (via REST API)** | Permite que os dados de qualidade do chão de fábrica (torque, posição) sejam imediatamente integrados ao sistema corporativo, fechando o *loop* de controle e validação de processo. |

### 5.3. Eficiência e Sustentabilidade (Manutenção Preditiva e Flexibilidade)

| Benefício Operacional | Mecanismo Arquitetural | Impacto na Linha de Produção |
| :--- | :--- | :--- |
| **Redução de Manutenção Corretiva** | **Sensores de Vibração/Temperatura (IFM)** | Possibilita a **Manutenção Preditiva (PdM)**. Ao detectar falhas incipientes (motores, mancais) antes da quebra, o sistema permite intervenções planejadas, convertendo paradas não programadas em paradas controladas. |
| **Agilidade e Integração de Dados** | **Middleware Node-RED** | Atua como um "tradutor universal" e orquestrador *low-code*. Permite que a fábrica adicione novos sensores, linhas ou mude a lógica de negócios **rapidamente**, sem precisar reprogramar os CLPs ou mexer nos sistemas legados (FIS/CobrA). |