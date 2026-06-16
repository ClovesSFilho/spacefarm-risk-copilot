# SpaceFarm Risk Copilot

POC de Inteligencia Artificial para monitoramento agricola orientado por dados climaticos e espaciais.

## Proposta

A economia espacial ja influencia a vida na Terra por meio de satelites, previsao climatica, monitoramento ambiental e analise de grandes volumes de dados. O SpaceFarm Risk Copilot demonstra como esses dados podem apoiar a agricultura: o sistema calcula um indice de risco para uma fazenda, classifica a situacao com Machine Learning e recomenda uma acao operacional.

## Problema

Produtores rurais lidam com variacoes de temperatura, chuva, radiacao solar, vento e umidade do solo. Essas informacoes existem, mas muitas vezes chegam de forma fragmentada e dificil de transformar em decisao. A proposta e criar uma camada simples de inteligencia que transforma dados em alerta pratico.

## Solucao

O projeto entrega um dashboard em Python que:

- le dados climaticos em CSV;
- calcula um indice de risco agricola;
- usa um classificador de Machine Learning para prever o nivel de risco;
- apresenta graficos e indicadores em uma interface Streamlit;
- gera recomendacoes automaticas;
- simula um alerta que poderia ser integrado a AWS SNS/Lambda.

## Arquitetura

```text
Dados climaticos/espaciais
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
Recomendacao + alerta operacional
```

Em uma versao produtiva, os dados locais poderiam ser substituidos por APIs meteorologicas, sensores IoT, imagens orbitais ou produtos de satelite. A camada de alerta poderia usar AWS Lambda e SNS.

## Tecnologias

- Python
- Streamlit
- Pandas
- Scikit-learn
- Plotly

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Estrutura

```text
spacefarm-risk-copilot/
├── app.py
├── data/
│   ├── climate_sample.csv
│   └── README.md
├── docs/
│   ├── architecture.html
│   └── screenshots/
├── reports/
│   └── SpaceFarm_Risk_Copilot_SubGS.md
├── src/
│   ├── alert_service.py
│   ├── model.py
│   ├── recommendations.py
│   └── risk_engine.py
└── requirements.txt
```

## Entregaveis

- Repositorio GitHub com codigo e documentacao.
- PDF unico com introducao, desenvolvimento, resultados esperados e conclusao.
- Video demonstrativo de ate 5 minutos, publicado como nao listado no YouTube.

## Limitacoes

Esta POC usa dados simplificados para manter a execucao viavel em contexto academico. O objetivo nao e substituir uma plataforma agricola profissional, mas demonstrar de forma funcional como IA, dados climaticos, automacao e arquitetura em nuvem podem ser combinados para resolver um problema real.

## Proximos passos

- Conectar uma API climatica real.
- Adicionar imagens orbitais ou indices de vegetacao.
- Integrar AWS SNS para envio real de alertas.
- Registrar historico de fazendas e talhoes em banco de dados.

