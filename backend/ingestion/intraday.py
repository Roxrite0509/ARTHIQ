import random
from ingestion.state_master import STATE_COORDS


def intraday_flows():
    return [
        {
            "type": "intraday",
            "state": s,
            "value": random.randint(-50, 50),
            "coords": c
        }
        for s, c in STATE_COORDS.items()
    ]
