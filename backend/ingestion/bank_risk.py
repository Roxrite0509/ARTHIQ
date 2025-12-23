import random
from ingestion.state_master import STATE_COORDS


def bank_risk():
    return [
        {
            "type": "bank_risk",
            "state": s,
            "risk": random.random(),
            "coords": c
        }
        for s, c in STATE_COORDS.items()
    ]
