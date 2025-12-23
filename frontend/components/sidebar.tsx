type Props = {
    mode: string
    setMode: (m: string) => void
}

export default function Sidebar({ mode, setMode }: Props) {
    const modes = [
        "sector",
        "intraday",
        "bank_risk",
        "policy"
    ]

    return (
        <div className="sidebar">
            <h2>ARTHIQ</h2>
            {modes.map(m => (
                <button
                    key={m}
                    className={mode === m ? "active" : ""}
                    onClick={() => setMode(m)}
                >
                    {m.toUpperCase()}
                </button>
            ))}
        </div>
    )
}
