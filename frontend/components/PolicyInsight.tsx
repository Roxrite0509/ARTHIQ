import { useEffect, useState } from "react"

export default function PolicyInsight() {
    const [data, setData] = useState<any>(null)

    useEffect(() => {
        fetch("http://localhost:8000/api/policy/insight")
            .then(res => res.json())
            .then(setData)
    }, [])

    if (!data) return <div>Loading policy insight...</div>

    return (
        <div className="insight-box">
            <h3>{data.title}</h3>

            <p><b>Total Money:</b> ₹{data.money_involved_cr} Cr</p>

            <ul>
                {data.implications.map((i: any, idx: number) => (
                    <li key={idx}>
                        <b>{i.sector}</b>: {i.impact} — {i.why}
                    </li>
                ))}
            </ul>

            <hr />
            <p><b>What this means:</b></p>
            <p>{data.explanation}</p>
        </div>
    )
}
