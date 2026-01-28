# S4_BOM.md

## Informações Gerais
- Este arquivo deve estar dentro da pasta "Docs de Negócios" do GitHub do Grupo, dedicada a esta Sprint: "Sprint 4"
- Mantenha a consistência terminológica com o TAPI
- Insira as figuras como .png e tabelas no próprio .md
- Cite obrigatoriamente as fontes usadas ao longo do texto – se houver, em uma seção de "Referências" ao final do arquivo. Para isso, utilize as normas ABNT ou APA

## Estrutura do Relatório

### 1. Lista de Componentes

A seguir está a lista consolidada de hardware, software, serviços e infraestrutura utilizados ou necessários para implantação industrial do sistema IoT de rastreabilidade.

#### 1.1 Tabela Geral de Componentes (BOM Consolidado Industrial)

| Categoria          | Componente / Hardware / Software / Serviço                         | Quantidade (Industrial) | Custo Unitário (R$)    | Fornecedor                    | Lead Time  | Observações                                                                  |
| ------------------ | ------------------------------------------------------------------ | ----------------------- | ---------------------- | ----------------------------- | ---------- | ---------------------------------------------------------------------------- |
| **Hardware**       | Antena UHF Industrial (Ex.: SICK RFU63x)                           | 6 unidades              | 8.000–12.000           | SICK Brasil                   | 30–45 dias | Antenas para leitura UHF em postos estratégicos (carroceria, bancos, rodas). |
| **Hardware**       | Leitor RFID/UHF Industrial (Ex.: SICK RFU62x / Balluff BIS U-600x) | 6 unidades              | 10.000–20.000          | SICK / Balluff                | 45 dias    | Leitores principais conectados aos gateways.                                 |
| **Hardware**       | Etiquetas RFID UHF padrão EPC Gen2                                 | 10.000 unidades         | 0,90 – 2,50            | 3M / Confidex via importadora | 20 dias    | Etiquetas fixadas nos produtos e subconjuntos.                               |
| **Hardware**       | Gateway Industrial (Ex.: Siemens IOT2050)                          | 3 unidades              | 4.000–7.000            | Siemens Brasil                | 20–30 dias | Conexão entre leitores/antenas e RabbitMQ.                                   |
| **Hardware**       | Cabeamento Industrial (Ethernet blindado CAT6A)                    | 60 metros               | 25–40/m                | Furukawa / Prysmian           | Imediato   | Instalação fabril.                                                           |
| **Hardware**       | Suportes metálicos para antenas e leitores                         | 6 conjuntos             | 300–600                | Fabricante local              | 7–10 dias  | Necessários para montagem adequada nos postos.                               |
| **Infraestrutura** | Servidor IBM Power – ambiente de produção                          | 1 existente             | —                      | IBM                           | —          | Já disponível no ambiente VW.                                                |
| **Infraestrutura** | Banco de dados DB2 (VW)                                            | 1 instância             | —                      | IBM                           | —          | Infra nativa utilizada para tabelas corporativas.                            |
| **Infraestrutura** | Servidor Docker + Node-RED                                         | 1 instância             | —                      | Ambiente VW                   | —          | Container com fluxo de ingestão e tratamento.                                |
| **Software**       | Node-RED (Docker image)                                            | 1                       | Gratuito               | Open Source                   | Imediato   | Integrado com RabbitMQ e pipelines.                                          |
| **Software**       | RabbitMQ                                                           | 1 instância             | Gratuito               | Open Source                   | Imediato   | Broker padrão da arquitetura VW.                                             |
| **Software**       | Supabase (PostgreSQL gerenciado)                                   | 1 instância             | Plano Pro (~R$100/mês) | Supabase                      | Imediato   | Ambiente para telemetria incremental.                                        |
| **Software**       | Python 3.10 (módulo de processamento IoT)                          | —                       | Gratuito               | Python                        | Imediato   | Script de processamento via RabbitMQ → Supabase.                             |
| **Serviços**       | Mão de obra de instalação industrial                               | 2 técnicos × 2 dias     | 1.500 – 2.500/dia      | Integrador local              | 10–15 dias | Instalação física e configuração.                                            |
| **Serviços**       | Configuração e programação de gateways                             | 1 técnico × 1 dia       | 1.000 – 2.000          | Integrador SICK/Balluff       | 10 dias    | Parametrização e testes.                                                     |

---

### 2. Classificação por Categoria

#### 2.1 Hardware
- Antenas UHF industriais
- Leitores RFID/UHF
- Etiquetas UHF RFID
- Gateway Siemens IOT2050
- Cabeamento industrial
- Suportes mecânicos

#### 2.2 Software
- Node-RED
- RabbitMQ
- Python (módulo de telemetria)
- Supabase
- Docker

#### 2.3 Serviços
- Integração e instalação
- Certificação e testes
- Configuração de readers
- Suporte técnico do integrador

#### 2.4 Infraestrutura
- IBM Power (VW)
- Banco DB2
- Rede fabril industrial
- Containers Docker
- Ambiente cloud Supabase

### 3. Análise de Custo
- Custo total por categoria
- Considerações sobre disponibilidade
- Restrições logísticas (Brasil)

#### 3.1 Custo Total por Categoria (Cenário Volkswagen)
| Categoria      | Custo Estimado (R$)                           |
| -------------- | --------------------------------------------- |
| Hardware       | ~ R$ 120.000 – 180.000                    |
| Software       | ~ R$ 0 – 6.000/ano (Supabase)             |
| Serviços       | ~ R$ 8.000 – 15.000                       |
| Infraestrutura | Sem custo adicional (uso da estrutura VW) |

**Custo Total Estimado:** De R$130.000 a R$200.000 para implantação industrial do módulo de rastreamento UHF + IoT.

#### 3.2 Considerações sobre Disponibilidade
SICK e Balluff possuem operação no Brasil, tendo menor risco de importação, as etiquetas RFID EPC Gen2 podem ser adquiridas localmente (Confidex, 3M). Por fim, Gateways Siemens IOT2050 possuem disponibilidade em estoque via Siemens-Brasil ou integradores.

#### 3.3 Restrições Logísticas para Implantação no Brasil
Sensores/leitores UHF acima de 902–928 MHz dependem de certificação ANATEL, mas SICK/Balluff já possuem homologação. Os equipamentos importados têm lead time maior por retenção em alfândega. As peças metálicas customizadas (suportes) devem ser fabricadas localmente, além disso, a rede fabril Volkswagen exige cabeamento blindado e certificação EMC.

### 4. Referências
- TAPI Oficial Volkswagen 2025.

- SICK AG. RFU63x UHF Reader Series. Disponível em: https://www.sick.com

- Siemens. IOT2050 Edge Gateway. Disponível em: https://www.siemens.com

- Confidex. UHF RFID Label Portfolio. Disponível em: https://www.confidex.com

- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. Sistemas RFID – Especificações Gerais. ABNT NBR 17070.

- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. Sistemas de Comunicação Industrial — Requisitos EMC. ABNT NBR IEC 61000.