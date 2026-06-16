# SpaceFarm Risk Copilot

POC de Inteligência Artificial para monitoramento agrícola orientado por dados climáticos e espaciais.

## Sobre o Projeto

Este projeto foi desenvolvido para a Atividade Substitutiva Global Solution 2026.1 da FIAP, no curso de Inteligência Artificial. A proposta responde ao desafio:

> Como a Inteligência Artificial e as tecnologias digitais podem transformar a nova economia espacial e gerar impacto positivo na Terra?

O SpaceFarm Risk Copilot demonstra como dados climáticos, sensores e informações derivadas de observação espacial podem apoiar decisões agrícolas. A aplicação calcula um índice de risco para uma fazenda, classifica a situação com Machine Learning e recomenda uma ação operacional.

## Integrante

- Cloves Silva Filho - RM 567250

## Problema

Produtores rurais lidam com variações de temperatura, chuva, radiação solar, vento e umidade do solo. Essas informações existem, mas muitas vezes chegam de forma fragmentada e difícil de transformar em decisão prática.

A proposta é criar uma camada simples de inteligência que transforma dados ambientais em leitura de risco, recomendação e alerta.

## Solução

O projeto entrega um dashboard em Python que:

- lê dados climáticos em CSV;
- calcula um índice de risco agrícola;
- usa um classificador de Machine Learning para prever o nível de risco;
- apresenta gráficos e indicadores em uma interface Streamlit;
- gera recomendações automáticas;
- simula um alerta que poderia ser integrado à AWS SNS/Lambda.

## Arquitetura

```text
Dados climáticos/espaciais
        |
        v
Pipeline Python + motor de risco
        |
        v
Modelo de Machine Learning
        |
        v
Dashboard Streamlit
        |
        v
Recomendação + alerta operacional
```

Em uma versão produtiva, os dados locais poderiam ser substituídos por APIs meteorológicas, sensores IoT, imagens orbitais ou produtos de satélite. A camada de alerta poderia usar AWS Lambda e SNS.

## Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Scikit-learn
- Plotly

## Estrutura de Pastas

```text
spacefarm-risk-copilot/
├── app.py
├── data/
│   ├── climate_sample.csv
│   └── README.md
├── docs/
│   ├── architecture.html
│   └── README.md
├── reports/
│   ├── SpaceFarm_Risk_Copilot_SubGS.md
│   ├── SpaceFarm_Risk_Copilot_SubGS.html
│   ├── SpaceFarm_Risk_Copilot_SubGS.pdf
│   └── README.md
├── src/
│   ├── alert_service.py
│   ├── model.py
│   ├── recommendations.py
│   ├── risk_engine.py
│   └── README.md
└── requirements.txt
```

## Como Executar o Código

Pré-requisitos:

- Python 3.10 ou superior
- `pip`

Passo a passo:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Depois de executar o comando, o Streamlit abrirá o dashboard no navegador.

## Links e Entregáveis

- Repositório GitHub: https://github.com/ClovesSFilho/spacefarm-risk-copilot
- Vídeo demonstrativo no YouTube: inserir link aqui
- Relatório em PDF: `reports/SpaceFarm_Risk_Copilot_SubGS.pdf`

## Decisões Técnicas

O projeto usa dados simplificados para manter a execução viável em contexto acadêmico. O objetivo não é substituir uma plataforma agrícola profissional, mas demonstrar, de forma funcional, como IA, análise de dados, dashboard e arquitetura em nuvem podem ser combinados para resolver um problema real.

O modelo escolhido foi Random Forest por ser simples de demonstrar, robusto para uma POC pequena e compatível com o nível de uma entrega acadêmica de primeiro ano.

## Próximos Passos

- Conectar uma API climática real.
- Adicionar imagens orbitais ou índices de vegetação.
- Integrar AWS SNS para envio real de alertas.
- Registrar histórico de fazendas e talhões em banco de dados.
