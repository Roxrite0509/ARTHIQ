def compute_market_state(snapshot):
    flows = snapshot["flows"]
    risks = snapshot["bank_risk"]
    sectors = snapshot["sector_rotation"]

    signals = []

    if flows["fii"] < -3000:
        signals.append({
            "type": "CAPITAL_OUTFLOW",
            "severity": "HIGH",
            "message": "Heavy FII selling detected"
        })

    if risks["banks"] > 0.7:
        signals.append({
            "type": "BANK_RISK",
            "severity": "ELEVATED",
            "message": "Banking sector stress rising"
        })

    if sectors["infra"] > 0.6:
        signals.append({
            "type": "SECTOR_MOMENTUM",
            "severity": "POSITIVE",
            "message": "Infrastructure showing strong rotation"
        })

    return {
        "signals": signals,
        "snapshot": snapshot
    }
