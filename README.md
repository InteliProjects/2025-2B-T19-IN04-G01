# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="https://res.cloudinary.com/dyhjjms8y/image/upload/v1759502495/inteli_pjgxcm.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width=40% height=40%></a>
</p>

<br>

# Projeto de Solução de Internet das Coisas para Automação Sustentável

## Sem Parar

## 👨‍🎓 Integrantes: 
- <a href="[www.linkedin.com/in/adrianapolicia]">[Adriana Polícia]</a>
- <a href="[www.linkedin.com/in/alexsander-dsbarbosa]">[Alexander Barbosa]</a>
- <a href="[www.linkedin.com/in/danilo-de-castro-neto]">[Danilo Neto]</a>
- <a href="[www.linkedin.com/in/gabriel-c-zanette]">[Gabriel Zanette]</a>
- <a href="[www.linkedin.com/in/hugo-montan-393b49175]">[Hugo Montan]</a>
- <a href="[www.linkedin.com/in/lu%C3%ADsa-mangini]">[Luísa Mangini]</a>
- <a href="[www.linkedin.com/in/maurihkorn1818]">[Mauri Korn]</a>


## 📜 Descrição

Este projeto faz parte do curso de **Administração Tech** do INTELI. O objetivo é desenvolver uma solução tecnológica que otimize processos de negócio em uma organização real, aplicando conceitos de administração, tecnologia e inovação.

**Parceiro e contexto:** setor **automobilístico (Volkswagen)**, com foco na **rastreabilidade e automação** para componentes **rodas e bancos**. Entregamos uma **arquitetura IoT completa** (camadas de *Perception*, *Communication* e *Application*), a **arquitetura administrativa** (contratos e decisões de negócio com fornecedores) e a **precificação** da infraestrutura em diferentes cenários (baixa escala, larga escala e importação), considerando impactos em **fluxo de caixa**, **logística** e **governança**.

A solução integra tecnologia e administração para melhorar **eficiência operacional**, **qualidade**, **visibilidade de dados** e **tomada de decisão**. O projeto contempla análise de processos, modelagem de negócio, KPIs, desenho técnico (draw.io), especificações contratuais, plano de custos e documentação executiva.

O funcionamento desta solução pode ser visto [neste vídeo](https://drive.google.com/file/d/1advhdS2_EL6LAFfjk8AQYdTE-U53k6jx/view?usp=sharing).

## 📁 Estrutura de pastas

- **assets/**: Imagens, diagramas (draw.io/diagrams.net) e elementos gráficos.
- **docs/**: Documentação por sprint e artefatos finais, incluindo:
  - `arquitetura-iot-projeto.md` – definição técnica + arquitetura administrativa (contratos/fornecedores).
  - `precificacao_infraestrutura_iot_detalhada.md` – **Perception layer** (sensores e controladores).
  - `precificacao_camadas_comunicacao_aplicacao.md` – **Communication & Application layers**.
  - (Outros: KPIs, matriz de riscos, EVTE/ROI, benchmarks, etc.)
- **src/**: Códigos/artefatos técnicos (ex.: flows do Node-RED, scripts de integração, simuladores OPC/MQTT).
- **README.md**: Guia geral do projeto.

## 🔧 Configuração para Desenvolvimento e Execução do Código

1. **Requisitos:**
   - **Node.js 18+** (para orquestração/local tooling).
   - **Python 3.10+** (scripts e utilitários).
   - **Docker 24+** (opcional; facilita a execução de serviços).
   - **draw.io/diagrams.net** (edição dos diagramas).
   - **Planilhas (Excel/Google Sheets)** para custos e KPIs.
   - **(Opcional)**: Cliente IBM DB2 / TIA Portal / simulador OPC UA, conforme escopo de testes.

2. **Instalação:**
   - Clone o repositório:  
     ```bash
     git clone [URL do repositório]
     cd [nome-do-projeto]
     ```
   - Instale dependências (se houver):  
     ```bash
     # Node (exemplo)
     cd src && npm install
     # Python (exemplo)
     python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
     ```

3. **Configuração:**
   - Variáveis de ambiente (exemplos):  
     ```bash
     export OPC_ENDPOINT="[opc.tcp://host:porta]"
     export MQTT_BROKER_URL="[mqtt://broker:1883]"
     export DB2_DSN="[dsn ou connection string]"
     ```
   - Parâmetros do projeto: defina **células**, **quantidade de CLPs/gateways**, **metragem de cabo**, e **cenário** (baixa/larga/importação) na planilha de custos em `docs/`.

4. **Execução:**
   - Orquestração local (exemplo com Node-RED):  
     ```bash
     npx node-red
     ```
   - Testes/Simulação (exemplos):  
     ```bash
     # Simular publicações MQTT
     python src/tools/publish_mqtt.py
     # Simular leitura OPC UA
     python src/tools/opc_reader.py
     ```

## 🚀 Funcionalidades

- **Rastreabilidade e telemetria** de rodas e bancos (sensores RFID/UHF, posição, vibração, temperatura).
- **Ingestão e integração** via **OPC UA / MQTT / REST** com gateways OT/TI.
- **Plataforma de aplicação** com **IBM Power (master/mirror)**, **PowerHA**, **DB2** e **Node‑RED** para orquestração.
- **Arquitetura administrativa**: contratos, SLAs e responsabilidades de fornecedores (Volkswagen ↔ fornecedores de rodas/bancos).
- **Análise de custos** por cenário (baixa/larga/importação) com impactos no **fluxo de caixa** e **logística**.
- **KPIs sugeridos**: OEE, lead time de abastecimento, taxa de falta de peças, MTBF/MTTR sensores, latência e integridade de dados, taxa de alertas resolvidos.

## 🗃 Histórico de Entregas

* **Sprint 1 — Setembro/2025**
  - Benchmarking de soluções IoT; Análise de Impacto Indústria 4.0.
  - Canvas de Proposta de Valor; Matriz de Riscos (v1).
* **Sprint 2 — Outubro/2025**
  - **Arquitetura IoT completa (perception/communication/application)** + diagrama **draw.io**.
  - **Arquitetura administrativa** (contratos com fornecedores; decisões estratégicas/operacionais/governança).
  - Matriz de Riscos (revisão).
* **Sprint 3 — Novembro/2025**
  - **Precificação por camadas**: sensores/controladores (**perception**), comunicação e aplicação.
  - **Cenários de custo** (baixa/larga/importação) + impactos no **fluxo de caixa** e **logística**.
  - Definição de **KPIs operacionais e econômicos** (rascunho).
* **Sprint 4 — Dezembro/2025**
  - **EVTE** (ROI, VPL, TIR) + **BOM** consolidada.
  - Matriz de Riscos (revisão).
* **Sprint 5 — Janeiro/2026**
  - Entrega final e apresentação executiva (documentação e demonstração).

## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/[seu-repositorio]">[Nome do Projeto]</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/[seu-repositorio]">INTELI, [Nomes dos Alunos]</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""></a></p>