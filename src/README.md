# Código-fonte

Esta pasta contém os módulos principais do SpaceFarm Risk Copilot.

- `risk_engine.py`: calcula o índice de risco agrícola com base nas variáveis climáticas.
- `model.py`: treina o classificador de Machine Learning e prevê o nível de risco mais recente.
- `recommendations.py`: transforma o risco calculado em uma recomendação operacional.
- `alert_service.py`: simula o payload de alerta que poderia ser enviado por uma camada futura de automação.

O arquivo `app.py`, na raiz do projeto, integra esses módulos em um dashboard Streamlit.
