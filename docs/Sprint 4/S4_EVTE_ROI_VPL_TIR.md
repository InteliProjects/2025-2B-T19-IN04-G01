# S4_EVTE_ROI_VPL_TIR.xlsx

## Informações Gerais
- A entrega deverá ser feita no GitHub, em formato de texto, dentro da pasta do GitHub do Grupo, dedicada a esta Sprint: "Sprint 4"
- Mantenha a consistência terminológica com o TAPI
- Insira as figuras como .png e tabelas no próprio .md
- Cite obrigatoriamente as fontes usadas ao longo do texto – se houver, em uma seção de "Referências" ao final do arquivo. Use a norma ABNT.

## Estrutura do Relatório

### 1. Custos de Implementação
Nesta seção é apresentado o investimento necessário para aquisição, instalação e manutenção inicial do sistema IoT proposto para a Volkswagen, considerando sensores industriais, controladores, gateways, infraestrutura de comunicação, servidores e software, conforme detalhado na Bill of Materials.

A opção adotada foi o cenário conservador de custos (ou pessimista), utilizando o valor máximo estimado para implantação: R$ 200.000,00.
Essa escolha garante que toda a análise financeira será precavida, reduzindo o risco de superestimar retornos ou subestimar despesas.

#### 1.1 Lista de Materiais (Resumo)
| Categoria                                                | Descrição                        | Quantidade | Custo unitário (R$) | Custo total (R$)  |
| -------------------------------------------------------- | -------------------------------- | ---------- | ------------------- | ----------------- |
| Sensores industriais (torque, posição, vibração)         | Equipamentos HBM / Balluff / IFM | 16+        | ~55.000             | 55.000            |
| Identificação e rastreabilidade                          | Leitores UHF SICK RFU620         | 4          | ~21.000             | 84.000            |
| Controladores Siemens                                    | PLCs S7-1500 e S7-1200           | 6          | ~12.000             | 72.000            |
| Atuação                                                  | Chaves Atlas Copco               | 4          | ~80.000             | 80.000            |
| Comunicação                                              | Switches e cabos PROFINET        | —          | —                   | 20.000            |
| Gateway OT/TI                                            | Siemens IOT2050                  | 1          | ~5.300              | 5.300             |
| Servidor/Aplicação                                       | IBM Power + Licenças             | —          | —                   | 300.000*          |
| **Total estimado (implantação realista para piloto VW)** | —                                | —          | —                   | **R$ 200.000,00** |

### 2. Aquisição dos materiais.
#### 2.1 Conversão de Taxa Anual para Taxa Mensal
i (mensal) = (1 + 0,15)^(1/12) - 1

i (mensal) = 1,171 %

#### 2.2 Cálculo das Parcelas
- PV = 200.000
- i = 0,01171
- n = 12


PMT = 200.000 * ((0,01171(1+0,01171)^(12)) / ((1+0,01171)^(12) - 1))

**PMT:** R$18.043,43 (Valor Mensal da Parcela)

### 3. Definição do Lucro (Benefício) Líquido Mensal
- Investimento: R$200.000
- Tempo: 4 Meses
- Lucro Mensal = R$200.000 / 4 
- **Lucro Mínimo Mensal Mínimo:** R$50.000
Assim, o projeto deve gerar pelo menos R$50.000 por mês, para que o investimento se pague em 4 meses. 

### 4. Cálculo e interpretação do ROI
- Calcule o ROI do projeto utilizando os valores encontrados anteriormente e interprete o significado do resultado obtido, explicando o que ele representa em relação ao investimento.

- Ganho Total = 12 (meses) * R$50.000 (Lucro minimo) = R$600.000
- Investimento = R$200.00

- **ROI** = (R$600.000 - R$200 000) / R$200.000
- **ROI =** 200%

Dessa forma, a cada R$1 investido, a Volkswagen terá R$2 de lucro (fora o valor inicial), ou seja, a solução demonstra ser sustentável financeiramente, além do ganho tecnológico e operacional.


### 5. Determinação do VPL e TIR
#### 5.1 Conversão de TMA para Mensal

Taxa Anual escolhida = 12% a.a

Taxa Mensal = (1 + 0,12)^(1/12) - 1

**Taxa Mensal =** 0,0095 (0,95%)

#### 5.2 Fluxo de Caixa Considerado
- Mês 0 = - 200.000
- Meses 1 a 12 = + 50.000 (cada mês)

#### 5.3 Cálculo do VPL
| Mês | Fluxo de Caixa (FC) | Valor Presente (VP) |
| :---: | :---: | :---: |
| 0 | -R$ 200.000,00 | -R$ 200.000,00 |
| 1 | R$ 50.000,00 | R$ 49.529,47 |
| 2 | R$ 50.000,00 | R$ 49.063,37 |
| 3 | R$ 50.000,00 | R$ 48.601,65 |
| 4 | R$ 50.000,00 | R$ 48.144,28 |
| 5 | R$ 50.000,00 | R$ 47.691,22 |
| 6 | R$ 50.000,00 | R$ 47.242,41 |
| 7 | R$ 50.000,00 | R$ 46.797,83 |
| 8 | R$ 50.000,00 | R$ 46.357,44 |
| 9 | R$ 50.000,00 | R$ 45.921,19 |
| 10 | R$ 50.000,00 | R$ 45.489,04 |
| 11 | R$ 50.000,00 | R$ 45.060,96 |
| 12 | R$ 50.000,00 | R$ 44.636,91 |
| VPL Total | | R$ 364.535,77 |

Como o VPL é > 0, significa que o projeto gera valor econômico.

#### 5.4 TIR Aproximada
TIR a 20% a.a = VPL Positivo

TIR a 70% a.a = VPL próximo a 0

**TIR aproximada = 65% a 70%**

Essa TIR é muito superior a TMA de 12% a.a, isso quer dizer que o projeto é consideravelmente mais lucrativo que o retorno mínimo esperado.

### 6. Conclusão sobre a análise financeira.
O projeto demonstra ser muito viável economicamente, sendo capaz de gerar valor muito acima do investimento inicial e com retorno extremamente acelerado. Em um contexto de investimento de R$120 mil a R$200 mil, o sistema IoT oferece ganhos diretos em: continuidade operacional, redução de falhas, prevenção de paradas não planejadas e precisão no controle de qualidade.

### 7. Referências
- Slimstock. Lista de materiais (BOM): guia completo. Disponível em:
https://www.slimstock.com/pt/blog/lista-de-materiais-bom/
Acesso em: 04 dez. 2025.

- Siemens, IBM, Balluff, SICK, HBM — Fichas técnicas e valores estimados por mercado internacional (2025).

- ABNT NBR 6023:2018.
