import plotly.graph_objects as go

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 8, 12, 20]

# Create area chart using Scatter with fill='tozeroy'
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    fill='tozeroy',  # Fill to x-axis
    mode='lines+markers',
    line_color='royalblue',
    name='Data'
))

# Layout
fig.update_layout(
    title='Area Chart with Plotly',
    xaxis_title='X Axis',
    yaxis_title='Y Axis'
)

fig.show()
