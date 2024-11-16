import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Datos para 10 elementos
algorithms_10 = ["Burbuja Mejorado", "Burbuja Normal", "Insercción", "Selección"]
times_10 = [13700, 10800, 14000, 17100]

# Datos para 1000 elementos
algorithms_1000 = ["Burbuja Mejorado", "Burbuja Normal", "Insercción", "Selección"]
times_1000 = [10208200, 9853600, 4839700, 5079600]

# Datos para 100000 elementos
algorithms_100000 = ["Burbuja Mejorado", "Burbuja Normal", "Insercción", "Selección"]
times_100000 = [301300, 303500, 58300, 161400]

# Datos para 5000 elementos
algorithms_5000 = ["Burbuja Mejorado", "Burbuja Normal", "Insercción", "Selección"]
times_5000 = [53477400, 24708300, 19050900, 14533300]

# Datos para 10000 elementos
algorithms_10000 = ["Burbuja Mejorado", "Burbuja Normal", "Insercción", "Selección"]
times_10000 = [91500600, 93626300, 26410600, 24038800]

# Datos para 30000 elementos
algorithms_30000 = ["Burbuja Mejorado", "Burbuja Normal", "Insercción", "Selección"]
times_30000 = [1525273900, 1000624800, 296172700, 138437500]

fig = make_subplots(
    rows=1, cols=6, 
    subplot_titles=("Tiempos para 10 elementos", "Tiempos para 1000 elementos", 
                    "Tiempos para 100000 elementos", "Tiempos para 5000 elementos", 
                    "Tiempos para 10000 elementos", "Tiempos para 30000 elementos")
)

fig.add_trace(go.Scatter(
    x=algorithms_10,
    y=times_10,
    mode='lines+markers',
    fill='toself',
    line=dict(color='#1f77b4', width=4),
    marker=dict(color='#ff7f0e', size=10, symbol='circle'),
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=algorithms_1000,
    y=times_1000,
    mode='lines+markers',
    fill='toself',
    line=dict(color='#17becf', width=4),
    marker=dict(color='#ff7f0e', size=10, symbol='circle'),
), row=1, col=2)

fig.add_trace(go.Scatter(
    x=algorithms_100000,
    y=times_100000,
    mode='lines+markers',
    fill='toself',
    line=dict(color='#9467bd', width=4),
    marker=dict(color='#ff7f0e', size=10, symbol='circle'),
), row=1, col=3)

fig.add_trace(go.Scatter(
    x=algorithms_5000,
    y=times_5000,
    mode='lines+markers',
    fill='toself',
    line=dict(color='#8c564b', width=4),
    marker=dict(color='#ff7f0e', size=10, symbol='circle'),
), row=1, col=4)

fig.add_trace(go.Scatter(
    x=algorithms_10000,
    y=times_10000,
    mode='lines+markers',
    fill='toself',
    line=dict(color='#e377c2', width=4),
    marker=dict(color='#ff7f0e', size=10, symbol='circle'),
), row=1, col=5)

fig.add_trace(go.Scatter(
    x=algorithms_30000,
    y=times_30000,
    mode='lines+markers',
    fill='toself',
    line=dict(color='#7f7f7f', width=4),
    marker=dict(color='#ff7f0e', size=10, symbol='circle'),
), row=1, col=6)

fig.update_layout(
    title="Comparación de Tiempos de Ordenación",
    plot_bgcolor='#f4f4f4',
    paper_bgcolor='#ffffff',
    font=dict(family="Arial, sans-serif", size=14, color='#333333'),
    template="plotly_dark",
)

fig.show()
