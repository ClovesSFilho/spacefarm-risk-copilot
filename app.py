from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

from src.alert_service import simulate_alert
from src.model import predict_latest_risk, train_classifier
from src.recommendations import summarize_decision
from src.risk_engine import enrich_with_risk


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DATA = BASE_DIR / "data" / "climate_sample.csv"


st.set_page_config(
    page_title="SpaceFarm Risk Copilot",
    page_icon="🚜",
    layout="wide",
)


@st.cache_data
def load_data(uploaded_file=None) -> pd.DataFrame:
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_csv(DEFAULT_DATA)
    data["date"] = pd.to_datetime(data["date"])
    return enrich_with_risk(data)


st.title("SpaceFarm Risk Copilot")
st.caption("IA aplicada a dados climáticos e espaciais para antecipar risco agrícola na Terra.")

with st.sidebar:
    st.header("Entrada")
    uploaded = st.file_uploader("Enviar CSV climático", type=["csv"])
    st.markdown("A demonstração usa dados de exemplo de Campo Grande/MS.")

data = load_data(uploaded)
model = train_classifier(data)
latest = data.iloc[-1]
decision = summarize_decision(latest)
prediction = predict_latest_risk(model, data)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Risco atual", decision["nivel"], f"score {latest['risk_score']}")
col2.metric("Classificação ML", prediction)
col3.metric("Umidade do solo", f"{latest['soil_moisture_pct']}%")
col4.metric("Temperatura", f"{latest['temperature_c']} °C")

st.subheader("Leitura operacional")
st.write(decision["justificativa"])
st.info(decision["acao"])

chart = px.line(
    data,
    x="date",
    y="risk_score",
    color="risk_level",
    markers=True,
    title="Evolução do índice de risco agrícola",
)
chart.update_layout(xaxis_title="Data", yaxis_title="Índice de risco")
st.plotly_chart(chart, use_container_width=True)

left, right = st.columns([1.2, 1])
with left:
    st.subheader("Dados monitorados")
    st.dataframe(data.sort_values("date", ascending=False), use_container_width=True)

with right:
    st.subheader("Alerta simulado")
    alert_text = simulate_alert(
        location=str(latest["location"]),
        risk_level=decision["nivel"],
        action=decision["acao"],
    )
    st.code(alert_text)
    st.caption(
        "Em produção, essa camada poderia usar AWS Lambda + SNS para enviar e-mail ou SMS."
    )

st.subheader("Arquitetura da POC")
st.markdown(
    """
1. Dados climáticos e espaciais entram no pipeline.
2. O motor calcula um índice de risco agrícola.
3. Um modelo de ML classifica o risco como baixo, médio ou alto.
4. O dashboard transforma a classificação em decisão operacional.
5. Um serviço de alerta pode notificar a equipe da fazenda.
    """
)
