# Arthiq  
**Economic Intelligence, Mapped. Explained. Actionable.**

---

## What Arthiq Is

Arthiq is a **real-time economic and market intelligence platform** that transforms financial, macroeconomic, and capital-flow data into **clear, explainable insights**.

Instead of dumping charts or opaque AI predictions, Arthiq answers:

> **What is happening right now, why it is happening, and what it means.**

---

## Why Arthiq Exists

Modern markets fail in three fundamental ways:

- **Data overload without interpretation**
- **Lagging indicators that react after damage is done**
- **Black-box AI with no accountability**

Arthiq fixes this by combining **deterministic market logic** with **explainable AI interpretation** — not fake prediction engines.

---

## Core Principle

**Data → Signal → Insight → Action**

Every output in Arthiq can be traced back to:

- Raw data  
- Computed signals  
- Clear reasoning  

Nothing is hidden. Nothing is hand-waved.

---

## Key Features

### 🌍 Interactive Economic Intelligence Map
- Visualizes:
  - Capital inflows and outflows
  - Sector strength and weakness
  - Volatility and stress clusters
  - Regional momentum shifts
- All values are dynamically computed — **no static heatmaps**.

### 📈 Market Signal Engine
Arthiq computes:
- Price momentum and trend shifts  
- Volume and liquidity anomalies  
- Relative strength across regions and sectors  
- Correlation breakdowns  
- Macro → market influence mapping  

Signals are **deterministic, auditable, and explainable**.

### 🧠 Explainable AI Insights
LLMs are used strictly for:
- Interpreting signals  
- Explaining causality  
- Translating data into human reasoning  

❌ No prediction hallucinations  
❌ No black-box decision making  

### 🚨 Context-Aware Alerts
- Capital rotation detection  
- Regime and sentiment shifts  
- Risk escalation warnings  
- Macro shock propagation  

Every alert includes **context and reasoning**, not just numbers.

---

## Architecture Philosophy

Arthiq is built as **economic infrastructure**, not a demo dashboard.

- Modular and extensible design  
- Clear separation of concerns  
- No import hacks  
- No monolithic AI blobs  
- Every insight traceable to logic or data  

---

## Tech Stack

### Backend
- **FastAPI**
- **Python**
- Custom modules for:
  - Market & macro data ingestion
  - Signal computation and comparisons
  - Time-series and graph retrieval
  - Explainable AI interpretation

### Frontend
- **React / Next.js**
- Interactive map interface
- Insight and alert panels
- Designed for dashboards and simulations

---

## Project Structure

```text
backend/
 ├─ ingestion/        # Market & macro data sources
 ├─ analysis/         # Signals, metrics, comparisons
 ├─ retrieval/        # Time-series & graph access
 ├─ ai/               # Explainable AI layer
 └─ main.py           # FastAPI entry point

frontend/
 ├─ components/       # Map, insight panels, alerts
 ├─ pages/            # Application routes
 ├─ services/         # API clients
 └─ styles/           # UI styling
