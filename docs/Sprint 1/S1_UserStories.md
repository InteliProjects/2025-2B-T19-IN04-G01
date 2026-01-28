# User Stories
As user stories foram elaboradas para transformar as necessidades das personas em requisitos funcionais claros. Cada história evidencia quem é o usuário, qual é seu objetivo e qual benefício busca alcançar. Dessa forma, garantimos que o desenvolvimento do dashboard esteja alinhado às demandas reais dos diferentes perfis envolvidos no processo logístico.

--- 

## Persona: Laura Mendes (Analísta de Logística)
### User Story 1: Monitoramento de Consumo Diário
Como analista de logística, eu quero visualizar o consumo médio diário de peças por modelo de veículo, para que eu possa antecipar necessidades de reposição.

Critérios de Aceite:
- O sistema deve apresentar gráficos de consumo segmentados por modelo.
- O usuário deve conseguir selecionar o período de análise (dia, semana, mês).

### User Story 2: Alertas Automáticos de Estoque
Como analista de logística, eu quero receber alertas quando um item atingir o nível mínimo de segurança, para que eu possa acionar a reposição antes da falta.

Critérios de Aceite:
- O sistema deve emitir notificações visuais e sonoras quando um item chegar ao limite.
- O usuário deve poder configurar os níveis mínimos de estoque.

### User Story 3: Relatórios Rápidos para Reuniões
Como analista de logística, eu quero gerar relatórios automáticos do dashboard, para que eu possa compartilhar dados atualizados nas reuniões diárias.

Critérios de Aceite:
- O sistema deve exportar relatórios em PDF ou Excel com dados de consumo.
- O relatório deve incluir destaques de itens em risco de falta.

---

## Persona: Ricardo Oliveira (Gerente de Estoque)
### User Story 1: Visão Macro do Estoque
Como gerente de estoque, eu quero ter uma visão consolidada dos níveis de peças, para que eu possa decidir sobre ajustes de compras.

Critérios de Aceite:
- O sistema deve apresentar o estoque total por peça e por modelo.
- O painel deve destacar itens dentro, acima ou abaixo do nível ideal.

### User Story 2: Indicadores de Giro e Cobertura
Como gerente de estoque, eu quero acompanhar indicadores de giro e dias de cobertura, para que eu possa equilibrar custo e disponibilidade.

Critérios de Aceite:
- O sistema deve calcular automaticamente o giro de estoque e a cobertura média.
- O painel deve permitir comparar indicadores atuais com históricos.

### User Story 3: Relatórios Consolidados para Diretoria
Como gerente de estoque, eu quero extrair relatórios consolidados mensais, para que eu possa apresentar resultados à diretoria.

Critérios de Aceite:
- O sistema deve consolidar dados do mês em formato gráfico e tabular.
- O relatório deve incluir redução de excessos e ocorrência de faltas.

---

## Persona: Carlos Pereira (Supervisor de Logística de Produção)
### User Story 1: Planejamento de Reposição no Turno
Como supervisor de logística, eu quero consultar rapidamente o dashboard no início do turno, para que eu possa planejar reposições imediatas.

Critérios de Aceite:
- O painel deve mostrar a situação atual do estoque de peças críticas.
- O sistema deve destacar em vermelho itens que demandam ação urgente.


### User Story 2: Priorização de Tarefas do Almoxarifado
Como supervisor de logística, eu quero identificar quais peças estão críticas, para que eu possa priorizar as atividades da equipe.

Critérios de Aceite:
- O sistema deve listar os itens em ordem de criticidade.
- O supervisor deve conseguir gerar uma lista de reposições priorizadas.


### User Story 3: Status Visual de Estoque
Como supervisor de logística, eu quero visualizar o status por cores (verde, amarelo, vermelho), para que eu possa tomar decisões rápidas sem analisar números detalhados.

Critérios de Aceite:
- O painel deve exibir indicadores de cores baseados nos níveis de estoque.
- O usuário deve poder personalizar os limites que definem cada cor.

--- 

## Persona: Fernanda Costa (Representante de Fornecedor Interno)
### User Story 1: Monitoramento do Consumo em Tempo Real
Como representante de fornecedor, eu quero acompanhar o consumo de rodas dentro da fábrica, para que eu possa programar novas entregas no momento certo.

Critérios de Aceite:
- O painel deve exibir o saldo atual de peças disponíveis na planta.
- O sistema deve atualizar o consumo em tempo real conforme a produção avança.

### User Story 2: Ajuste de Entregas por Aumento de Produção
Como representante de fornecedor, eu quero ajustar a frequência das entregas quando houver aumento repentino na produção, para que não falte estoque.

Critérios de Aceite:
- O painel deve sinalizar variações de consumo fora do previsto.
- O sistema deve permitir visualizar tendências de aumento no uso de peças.

### User Story 3: Histórico de Fornecimento para Avaliação
Como representante de fornecedor, eu quero acessar históricos de fornecimento, para que eu possa demonstrar minha performance em reuniões com a Volkswagen.

Critérios de Aceite:
- O sistema deve armazenar dados de entregas e consumo por período.
- O usuário deve poder exportar gráficos e relatórios de desempenho.
