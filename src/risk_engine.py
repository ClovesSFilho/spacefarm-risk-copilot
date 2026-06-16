from __future__ import annotations

import pandas as pd


def normalize(value: float, min_value: float, max_value: float) -> float:
    if max_value == min_value:
        return 0.0
    score = (value - min_value) / (max_value - min_value)
    return max(0.0, min(1.0, score))


def classify_score(score: float) -> str:
    if score >= 70:
        return "Alto"
    if score >= 40:
        return "Médio"
    return "Baixo"


def calculate_risk_score(row: pd.Series) -> float:
    heat = normalize(row["temperature_c"], 26, 38)
    drought = 1 - normalize(row["soil_moisture_pct"], 15, 60)
    rain_deficit = 1 - normalize(row["precipitation_mm"], 0, 25)
    radiation = normalize(row["solar_radiation_wm2"], 480, 850)
    wind = normalize(row["wind_kmh"], 8, 30)

    stage_weight = {
        "vegetative": 0.9,
        "flowering": 1.15,
        "fruiting": 1.1,
        "maturation": 1.0,
    }.get(str(row.get("crop_stage", "")).lower(), 1.0)

    weighted_score = (
        heat * 0.26
        + drought * 0.28
        + rain_deficit * 0.18
        + radiation * 0.16
        + wind * 0.12
    ) * 100

    return round(min(weighted_score * stage_weight, 100), 1)


def enrich_with_risk(data: pd.DataFrame) -> pd.DataFrame:
    enriched = data.copy()
    enriched["risk_score"] = enriched.apply(calculate_risk_score, axis=1)
    enriched["risk_level"] = enriched["risk_score"].apply(classify_score)
    return enriched
