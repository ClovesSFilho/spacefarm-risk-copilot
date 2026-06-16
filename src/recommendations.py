from __future__ import annotations

import pandas as pd


def generate_recommendation(row: pd.Series) -> str:
    risk_level = row["risk_level"]
    temp = row["temperature_c"]
    soil = row["soil_moisture_pct"]
    rain = row["precipitation_mm"]

    if risk_level == "Alto" and soil < 25 and temp >= 34:
        return "Acionar irrigação prioritária e enviar alerta técnico para monitoramento de estresse hídrico."
    if risk_level == "Alto":
        return "Enviar alerta operacional e revisar manejo nas próximas 24 horas."
    if risk_level == "Médio" and rain == 0:
        return "Monitorar tendência de seca e preparar irrigação preventiva."
    if risk_level == "Médio":
        return "Manter observação diária e comparar com previsão meteorológica."
    return "Condição controlada. Manter rotina de monitoramento."


def summarize_decision(row: pd.Series) -> dict[str, str]:
    return {
        "nivel": row["risk_level"],
        "acao": generate_recommendation(row),
        "justificativa": (
            f"Índice {row['risk_score']} calculado com temperatura de "
            f"{row['temperature_c']} °C, solo em {row['soil_moisture_pct']}% "
            f"e chuva de {row['precipitation_mm']} mm."
        ),
    }
