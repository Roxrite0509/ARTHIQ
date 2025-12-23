export default function InsightPanel({ signals, summary, flows }) {
    return (
        <div className="insight-panel">
            <h3>Live Market Intelligence</h3>

            <div className="alerts">
                {signals.map((s, i) => (
                    <div key={i} className={`alert ${s.severity.toLowerCase()}`}>
                        {s.message}
                    </div>
                ))}
            </div>

            <div className="flows">
                <h4>Capital Flow (₹ Cr)</h4>
                <p>FII: {flows.fii}</p>
                <p>DII: {flows.dii}</p>
            </div>

            <div className="explanation">
                <h4>What This Means</h4>
                <p>{summary}</p>
            </div>

            <div className="decision">
                <h4>Action Bias</h4>
                <p>
                    {flows.fii < 0
                        ? "Defensive positioning recommended"
                        : "Risk-on sentiment building"}
                </p>
            </div>
        </div>
    )
}
