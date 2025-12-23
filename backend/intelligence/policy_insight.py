def compute_policy_insight():
    # Hard facts (can later be scraped / APIs)
    budget_allocations = {
        "infrastructure": 184000,  # ₹ Cr
        "railways": 240000,
        "defence": 593000,
        "renewables": 35000
    }

    implications = []

    if budget_allocations["infrastructure"] > 150000:
        implications.append({
            "sector": "Infrastructure",
            "impact": "Positive",
            "why": "Sustained government capex spending"
        })

    if budget_allocations["railways"] > 200000:
        implications.append({
            "sector": "Railways",
            "impact": "Strong Positive",
            "why": "Order inflows for EPC & PSU players"
        })

    return {
        "title": "Union Budget Policy Impact",
        "money_involved_cr": sum(budget_allocations.values()),
        "implications": implications
    }
