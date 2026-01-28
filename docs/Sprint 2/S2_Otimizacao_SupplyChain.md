# S2_Otimizacao_SupplyChain.md

## Introdução

&emsp;&emsp;Um dos maiores princípios de qualquer fábrica da Volkswagen é o Just in Sequence (JIS), que combina o Just in Time (JIT) com a entrega de peças na sequência exata necessária para montagem. Esse modelo garante grande agilidade, fator essencial para a sobrevivência no mercado automotivo moderno. Cada minuto de parada na linha de produção pode gerar perdas significativas para a Volkswagen. Por esse motivo, o controle de estoque é uma das atividades mais importantes para manter a metodologia JIS funcionando. É fundamental que nunca faltem peças no estoque, mas, ao mesmo tempo, o excesso de estoque também representa desperdício de recursos.

&emsp;&emsp;Com base nesse contexto, o grupo Sem Parar desenvolveu um modelo algébrico de otimização da cadeia de suprimentos para otimizar a estocagem de rodas na planta da Volkswagen. O objetivo é minimizar a quantidade de rodas em estoque, garantindo o uso eficiente de recursos e a continuidade da produção.

### Tipos de rodas analisados

&emsp;&emsp;Foram analisados três tipos distintos de rodas:

41P — Virtus Alloy wheels 6J x 15  
C0V — Virtus Steel wheels 7J x 15  
CR4 — Saveiro Alloy wheels 6J x 15  

&emsp;&emsp;As variáveis x1, x2 e x3 representam, respectivamente, a quantidade de rodas de cada tipo.

<br>

## Parâmetros e variáveis utilizadas

&emsp;&emsp;Além das variáveis de decisão, foram definidos os seguintes parâmetros:

- Capacidade total do estoque `E_max`  
- Estoque inicial do dia `S_i`  
- Demanda mínima por tipo de roda `x1_min, x2_min, x3_min`  
- Demanda máxima de produção por tipo (136, 128, 168)

&emsp;&emsp;As demandas mínima e máxima foram calculadas a partir de dados reais de produção fornecidos pela Volkswagen. O uso desses parâmetros tem como objetivo equilibrar o sistema: evitar estoques tão baixos que causem paradas na linha e, ao mesmo tempo, impedir níveis excessivos que prejudiquem o fluxo de caixa da empresa.

<br>

## Formulação do modelo

&emsp;&emsp;A otimização foi realizada por meio de programação linear, implementada em Python com a biblioteca PuLP, amplamente usada para resolver problemas de minimização e maximização com funções objetivo e restrições lineares.  
O estudo foi aplicado sobre dois meses de dados reais do mix de produção, a partir dos quais foram estimadas as demandas mínima, máxima e média para os três tipos de rodas.

### Etapas da formulação
1. Definição das demandas mínima e máxima
As demandas máximas refletem a capacidade máxima de produção diária da Volkswagen. A partir dos dados fornecidos, foram obtidos os seguintes valores aproximados:
- 136 rodas tipo 41P
- 128 rodas tipo C0V
- 168 rodas tipo CR4

2. Cálculo das demandas mínimas
Para calcular as demandas mínimas, foram utilizados os dados da semana anterior ao período de análise. O objetivo dessa abordagem é capturar o comportamento recente da linha de montagem, refletindo possíveis oscilações de produção, paradas programadas e variações no mix de veículos. Dessa forma, o limite mínimo se mantém alinhado à realidade operacional e não a um cenário atípico.

As demandas mínimas foram expressas pelas variáveis:

```
x1_min, x2_min, x3_min
```

3. Função objetivo
Como o foco é minimizar o estoque total, a função objetivo foi definida como:
```
model += x1 + x2 + x3, "Estoque_minimo"
```

Essa função busca o ponto de equilíbrio entre atender à demanda e evitar o excesso de peças armazenadas.

4. Restrições do modelo
Foram adicionadas restrições com base nos valores de demanda mínima e máxima, além da capacidade máxima do estoque.

A Volkswagen informou que sua capacidade total de armazenamento é de 21.846 rodas, distribuídas entre 16 modelos diferentes.
Para estimar a capacidade apenas para os três modelos analisados, o total foi dividido por 16 e multiplicado por 3, resultando em aproximadamente 4.096 rodas, valor utilizado como limite de estoque.

- Restrições:
```
model += (x1 + x2 + x3) <= 4096, "Estoque_max"

model += x1 >= x1_min, "Demanda_min_x1"
model += x1 <= 136, "Demanda_max_x1"

model += x2 >= x2_min, "Demanda_min_x2"
model += x2 <= 128, "Demanda_max_x2"

model += x3 >= x3_min, "Demanda_min_x3"
model += x3 <= 168, "Demanda_max_x3"
```

## Execução e resultados
Após a formulação, o modelo foi executado com o comando:
```
model.solve()
```

O retorno do solver foi 1, indicando que uma solução ótima foi encontrada com sucesso.

Os resultados obtidos foram:

```
Status: Ótimo
Rodas de Liga Leve (x1): 16.0
Rodas de Aço (x2): 36.0
Rodas Esportivas (x3): 32.0
Estoque mínimo: 84.0
```

## Interpretação dos resultados
  Os valores de cada tipo de roda são iguais ou muito próximos às demandas mínimas, o que indica que o modelo atingiu o ponto de operação mais eficiente possível dentro das restrições impostas.
O sistema ajustou automaticamente a estocagem para manter apenas o mínimo necessário para sustentar a produção, evitando o excesso de peças sem comprometer a continuidade da linha.

  Esse comportamento está de acordo com o princípio Just in Sequence, pois garante o fluxo contínuo de montagem com estoque mínimo. Na prática, o modelo contribui para:

- Redução de custos logísticos e de armazenagem
- Melhor aproveitamento do espaço físico no armazém
- Menor imobilização de capital em estoque
- Aumento da previsibilidade e estabilidade na cadeia de suprimentos

## Teste do modelo e validação da solução
1. Verificação das restrições com a solução ótima
A solução encontrada foi:
```
x1 (41P) = 16
x2 (C0V) = 36
x3 (CR4) = 32
```

Esses valores respeitam todas as restrições impostas.

1.1 Restrição de capacidade de estoque:
```
(x1 + x2 + x3) ≤ 4096
(16 + 36 + 32) = 84 ≤ 4096 (restrição satisfeita).
```

1.2 Restrições de demanda mínima e máxima:
```
x1_min ≤ x1 ≤ 136
x2_min ≤ x2 ≤ 128
x3_min ≤ x3 ≤ 168
```

Substituindo os valores calculados de x1_min, x2_min, x3_min (obtidos a partir da análise da última semana de produção), verifica-se que:
- x1 é maior ou igual à demanda mínima de 41P e menor que o máximo diário.
- x2 é maior ou igual à demanda mínima de C0V e menor que o máximo diário.
- x3 é maior ou igual à demanda mínima de CR4 e menor que o máximo diário.

Todas as restrições foram atendidas, o que confirma que a solução é factível dentro do conjunto de condições definidas.

2. Análise de folgas (slack)
As folgas indicam o quanto sobra até o limite de cada restrição:

2.1 Folga da capacidade de estoque:
```
Folga_estoque = 4096 − (x1 + x2 + x3)
Folga_estoque = 4096 − 84 = 4012
```

Isso mostra que, dentro dos parâmetros atuais, o estoque máximo não está sendo pressionado. Como o objetivo é minimizar o estoque, o solver naturalmente puxa os valores para perto das demandas mínimas.

2.2 Folga das demandas máximas:
```
Folga_max_41P = 136 − x1
Folga_max_C0V = 128 − x2
Folga_max_CR4 = 168 − x3
```

2.3 Folga das demandas mínimas:
```
Folga_min_41P = x1 − x1_min
Folga_min_C0V = x2 − x2_min
Folga_min_CR4 = x3 − x3_min
```

  As folgas das demandas mínimas são pequenas ou nulas, o que reforça que o modelo está operando no nível mínimo seguro definido pelos dados históricos.

  A análise das folgas confirma que o modelo mantém o estoque no menor nível possível sem violar as demandas mínimas observadas na operação real.

3. Consistência com a realidade
A consistência do modelo com a operação real da Volkswagen pode ser observada em três pontos principais:

3.1 Compatibilidade com o Just in Sequence (JIS)
A solução mantém estoques mínimos por tipo de roda, o que está alinhado à filosofia JIS/JIT, evitando excesso de peças e ao mesmo tempo garantindo disponibilidade para atender a demanda recente.

3.2 Uso de dados reais
As demandas mínimas e máximas foram obtidas a partir de dados reais de produção de dois meses, incluindo a análise da última semana para definir os limites inferiores (x1_min, x2_min, x3_min).

3.3 Risco operacional
Como os valores ótimos estão próximos das demandas mínimas, o modelo é conservador: garante o mínimo necessário, mas não adiciona folgas adicionais. Em situações reais, essa lógica pode ser ajustada por meio da inclusão de fatores de segurança, variações de demanda ou lead time dos fornecedores.

4. Teste de cenários (análise de sensibilidade)
Para testar a robustez do modelo, foram simulados cenários alterando parâmetros-chave e observando o impacto na solução.

**Cenário 1:** Redução da capacidade de estoque
  Suposição: redução do limite de 4096 para um valor menor (por exemplo, 1000 rodas), simulando restrição física temporária no armazém.
Resultado esperado: como a solução ótima atual utiliza apenas 84 rodas, essa mudança não altera o resultado.
Interpretação: o modelo não é sensível à capacidade máxima nas condições atuais, pois o estoque mínimo exigido é muito inferior ao limite físico.

**Cenário 2:** Aumento das demandas mínimas
  Suposição: aumento de x1_min, x2_min e x3_min com base em um crescimento da produção ou mudança no mix de veículos.
Resultado esperado: se as novas demandas mínimas ainda respeitarem a capacidade máxima, o modelo ajustará x1, x2 e x3 para esses novos patamares. Caso ultrapassem a capacidade (4096), o modelo se tornará inviável (Status: Infeasible), indicando que, com os recursos atuais, não é possível atender o plano de produção.

**Cenário 3:** Alteração no mix de produção
  Suposição: aumento da participação de um tipo de roda, como CR4, refletindo maior produção da Saveiro.
Resultado esperado: o modelo direciona mais estoque para CR4, mantendo a lógica de estoque mínimo. Isso demonstra que o modelo responde de forma coerente a mudanças no mix de produção.

  Esses testes de cenário demonstram que o modelo responde de forma lógica às alterações nos parâmetros, sinaliza inviabilidade quando as restrições são incompatíveis com os recursos e pode ser usado como ferramenta de apoio à decisão para avaliar impactos de mudanças operacionais na planta.

## Conclusão final
  O modelo algébrico desenvolvido mostrou-se uma ferramenta eficaz para planejamento e controle de estoques sob restrições operacionais.
Pode ser expandido para incluir outros parâmetros, como lead time, custos logísticos, níveis de serviço e limitações de produção.
Além disso, sua estrutura modular em Python com PuLP permite integração futura com sistemas ERP e dashboards de controle para monitoramento em tempo real.

  A aplicação de programação linear mostra-se uma abordagem robusta para sustentar o modelo de produção Just in Sequence da Volkswagen, provomendo mais eficiência nas operações da linha e redução de custos.
