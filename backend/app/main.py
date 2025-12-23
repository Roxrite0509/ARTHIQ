from fastapi import FastAPI
from llm.policy_explain import explain_policy
from intelligence.policy_insight import compute_policy_insight
from fastapi import FastAPI, WebSocket
from app.ws import market_ws

app = FastAPI()


@app.websocket("/ws/market")
async def ws(ws: WebSocket):
    await market_ws(ws)


@app.get("/")
def health():
    return {"status": "ok"}


app = FastAPI()


@app.get("/api/policy/insight")
def policy_insight():
    insight = compute_policy_insight()
    insight["explanation"] = explain_policy(insight)
    return insight
