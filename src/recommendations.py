from __future__ import annotations

import pandas as pd


def generate_recommendation(row: pd.Series) -> str:
    risk_level = row["risk_level"]
    temp = row["temperature_c"]
    soil = row["soil_moisture_pct"]
    rain = row["precipitation_mm"]

    if risk_level == "Alto" and soil < 25 and temp >= 34:
        return "Acionar irrigacao prioritaria e enviar alerta tecnico para monitoramento de estresse hidrico."
    if risk_level == "Alto":
        return "Enviar alerta operacional e revisar manejo nas proximas 24 horas."
    if risk_level == "Medio" and rain == 0:
        return "Monitorar tendencia de seca e preparar irrigacao preventiva."
    if risk_level == "Medio":
        return "Manter observacao diaria e comparar com previsao meteorologica."
    return "Condicao controlada. Manter rotina de monitoramento."


def summarize_decision(row: pd.Series) -> dict[str, str]:
    return {
        "nivel": row["risk_level"],
        "acao": generate_recommendation(row),
        "justificativa": (
            f"Indice {row['risk_score']} calculado com temperatura de "
            f"{row['temperature_c']} C, solo em {row['soil_moisture_pct']}% "
            f"e chuva de {row['precipitation_mm']} mm."
        ),
    }

