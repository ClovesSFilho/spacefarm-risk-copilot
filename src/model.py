from __future__ import annotations

import pandas as pd

FEATURES = [
    "temperature_c",
    "humidity_pct",
    "precipitation_mm",
    "solar_radiation_wm2",
    "soil_moisture_pct",
    "wind_kmh",
]


def train_classifier(data: pd.DataFrame):
    try:
        from sklearn.ensemble import RandomForestClassifier
    except Exception:
        return None

    model = RandomForestClassifier(n_estimators=120, random_state=42, max_depth=4)
    model.fit(data[FEATURES], data["risk_level"])
    return model


def predict_latest_risk(model, data: pd.DataFrame) -> str:
    latest = data.tail(1)
    if model is None:
        return str(latest.iloc[0]["risk_level"])
    prediction = model.predict(latest[FEATURES])[0]
    return str(prediction)

