from fastapi import WebSocket
import asyncio
import json

from ingestion.sector import sector_events
from ingestion.intraday import intraday_flows
from ingestion.bank_risk import bank_risk
from ingestion.policy import policy_events


async def market_ws(ws: WebSocket):
    await ws.accept()
    while True:
        payload = {
            "sector": sector_events(),
            "intraday": intraday_flows(),
            "bank_risk": bank_risk(),
            "policy": policy_events()
        }
        await ws.send_text(json.dumps(payload))
        await asyncio.sleep(10)
