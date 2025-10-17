import plotly.graph_objects as go

def visualize_threat_map(origin_coords, target_coords, query, intent, deception, zone_coords):
    fig = go.Figure()

    # Origin → Target Line
    fig.add_trace(go.Scattergeo(
        lon=[origin_coords[1], target_coords[1]],
        lat=[origin_coords[0], target_coords[0]],
        mode='lines',
        line=dict(width=2, color='red'),
        name='Threat Path'
    ))

    # Origin Point
    fig.add_trace(go.Scattergeo(
        lon=[origin_coords[1]],
        lat=[origin_coords[0]],
        mode='markers+text',
        marker=dict(size=10, color='orange'),
        text=["Origin"],
        name='Origin'
    ))

    # Target Point
    fig.add_trace(go.Scattergeo(
        lon=[target_coords[1]],
        lat=[target_coords[0]],
        mode='markers+text',
        marker=dict(size=10, color='green'),
        text=["Target Zone"],
        name='Target'
    ))

    # Zone Saturation Markers
    for zone, coords in zone_coords.items():
        fig.add_trace(go.Scattergeo(
            lon=[coords[1]],
            lat=[coords[0]],
            mode='markers',
            marker=dict(size=6, color='blue'),
            name=f"{zone.title()} Zone"
        ))

    fig.update_layout(
        title=f"🛡️ Threat Map: {intent} | {deception}",
        geo=dict(
            scope='asia',
            projection_type='natural earth',
            showland=True,
            landcolor='rgb(243, 243, 243)',
            countrycolor='rgb(204, 204, 204)',
        ),
        margin=dict(l=0, r=0, t=30, b=0)
    )

    return fig
