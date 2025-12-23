import dynamic from "next/dynamic"
import { useEffect, useState } from "react"
import Sidebar from "../components/sidebar"

const IndiaMap = dynamic(
    () => import("../components/IndiaMap"),
    { ssr: false }
)

export default function Home() {
    const [mode, setMode] = useState("sector")
    const [data, setData] = useState<any[]>([])

    useEffect(() => {
        const ws = new WebSocket("ws://localhost:8000/ws/market")

        ws.onmessage = (e) => {
            const payload = JSON.parse(e.data)
            setData(payload[mode] || [])
        }

        return () => ws.close()
    }, [mode])

    return (
        <div className="layout">
            <Sidebar mode={mode} setMode={setMode} />
            <IndiaMap data={data} />
        </div>
    )
}

