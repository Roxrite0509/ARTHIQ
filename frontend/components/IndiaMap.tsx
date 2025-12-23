import { MapContainer, TileLayer, CircleMarker } from "react-leaflet"

type Event = {
    coords: [number, number]
    value?: number
    risk?: number
}

export default function IndiaMap({ data }: { data: Event[] }) {
    return (
        <MapContainer
            center={[22.5, 78.9]}
            zoom={5}
            style={{ height: "100vh", width: "100%" }}
        >
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />

            {data.map((e, i) => (
                <CircleMarker
                    key={i}
                    center={e.coords}
                    radius={Math.min(40, Math.abs(e.value ?? (e.risk ?? 0.3) * 50))}
                    pathOptions={{
                        color: "#00e5ff",
                        fillOpacity: 0.45
                    }}
                />
            ))}
        </MapContainer>
    )
}
