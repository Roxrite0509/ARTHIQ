from openai import OpenAI
client = OpenAI()


def explain_policy(insight):
    prompt = f"""
Explain this policy impact for a trader.
Do not add new data. Only explain.

{insight}
"""
    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )
    return res.choices[0].message.content
