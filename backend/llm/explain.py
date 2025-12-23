from openai import OpenAI
client = OpenAI()


def explain_state(state):
    prompt = f"""
You are a financial intelligence system.
Explain the following market signals in simple terms.
Do NOT invent data. Only explain.

Signals:
{state['signals']}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
