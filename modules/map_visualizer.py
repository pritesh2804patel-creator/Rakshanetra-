# map_visualizer.py — Chakra Pulse Overlay for Rakshanetra

import plotly.graph_objects as go

def visualize_threat_map(origin_coords, target_coords, query, intent, deception, zone_frequency=None):
    fig = go.Figure()

    # Origin marker
    fig.add_trace(go.Scattergeo(
        lon=[origin_coords[1]],
        lat=[origin_coords[0]],
        text=f"🟥 Origin: {query}",
        marker=dict(size=10, color="red"),
        name="Origin"
    ))

    # Target marker
    fig.add_trace(go.Scattergeo(
        lon=[target_coords[1]],
        lat=[target_coords[0]],
        text=f"🟧 Target Zone",
        marker=dict(size=12, color="orange"),
        name="Target"
    ))

    # Chakra pulses for frequently targeted zones
    if zone_frequency:
        for zone, (lat, lon) in zone_frequency.items():
            fig.add_trace(go.Scattergeo(
                lon=[lon],
                lat=[lat],
                text=f"🌀 {zone.title()} Zone",
                marker=dict(size=20, color="gold", opacity=0.4),
                name=f"{zone.title()} Pulse"
            ))

    # Map layout
    fig.update_layout(
        geo=dict(
            scope="asia",
            projection_type="natural earth",
            showland=True,
            landcolor="rgb(10,10,30)",
            bgcolor="rgb(0,0,0)",
            showocean=True,
            oceancolor="rgb(5,5,20)",
            showcountries=True,
            countrycolor="rgb(80,80,80)"
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgb(0,0,0)",
        plot_bgcolor="rgb(0,0,0)",
        showlegend=False
    )

    return fig
