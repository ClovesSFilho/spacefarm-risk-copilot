from __future__ import annotations


def build_alert_payload(location: str, risk_level: str, action: str) -> dict[str, str]:
    return {
        "channel": "simulated_aws_sns",
        "recipient": "farm-operations@example.com",
        "subject": f"SpaceFarm alerta: risco {risk_level}",
        "message": f"Local monitorado: {location}. Ação recomendada: {action}",
    }


def simulate_alert(location: str, risk_level: str, action: str) -> str:
    payload = build_alert_payload(location, risk_level, action)
    return (
        f"[SIMULADO] Canal: {payload['channel']} | "
        f"Destino: {payload['recipient']} | "
        f"Mensagem: {payload['message']}"
    )
