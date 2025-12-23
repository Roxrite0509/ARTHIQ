import random
from ingestion.state_master import STATE_COORDS

SECTORS = ["IT", "BANKING", "INFRA", "ENERGY"]


def sector_events():
    return [
        {
            "type": "sector",
            "state": s,
            "sector": random.choice(SECTORS),
            "value": random.randint(-100, 100),
            "coords": c
        }
        for s, c in STATE_COORDS.items()
    ]
