import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Function to check for local top
def rw_top(data: np.array, curr_index: int, order: int) -> bool:
    if curr_index < order * 2 + 1:
        return False
    k = curr_index - order
    v = data[k]
    return all(data[k + i] <= v and data[k - i] <= v for i in range(1, order + 1))

# Function to check for local bottom
def rw_bottom(data: np.array, curr_index: int, order: int) -> bool:
    if curr_index < order * 2 + 1:
        return False
    k = curr_index - order
    v = data[k]
    return all(data[k + i] >= v and data[k - i] >= v for i in range(1, order + 1))

# Identify local tops and bottoms
def rw_extremes(data: np.array, order: int):
    tops, bottoms = [], []
    for i in range(len(data)):
        if rw_top(data, i, order):
            tops.append((i - order, data[i - order]))  # (index, price)
        if rw_bottom(data, i, order):
            bottoms.append((i - order, data[i - order]))  # (index, price)
    return tops, bottoms

# Load Data
data = pd.read_csv('Nifty_Minute.csv')
data['date'] = pd.to_datetime(data['date'])
data = data.set_index('date')

# Detect tops and bottoms
tops, bottoms = rw_extremes(data['close'].to_numpy(), 10)

# Convert detected points to pandas DataFrame
tops_df = pd.DataFrame(tops, columns=['index', 'price'])
bottoms_df = pd.DataFrame(bottoms, columns=['index', 'price'])

# Create Plotly figure
fig = go.Figure()

# Add close price line
fig.add_trace(go.Scatter(
    x=data.index, y=data['close'], mode='lines', name="Close Price",
    line=dict(color='blue')
))

# Add tops as green dots with hover tooltips
fig.add_trace(go.Scatter(
    x=data.index[tops_df['index']], 
    y=tops_df['price'], 
    mode='markers', 
    marker=dict(color='green', size=8, symbol='triangle-up'),
    name="Tops",
    hoverinfo='text',
    text=[f"Top<br>Date: {data.index[i].strftime('%Y-%m-%d %H:%M')}<br>Price: {p:.2f}" for i, p in tops]
))

# Add bottoms as red dots with hover tooltips
fig.add_trace(go.Scatter(
    x=data.index[bottoms_df['index']], 
    y=bottoms_df['price'], 
    mode='markers', 
    marker=dict(color='red', size=8, symbol='triangle-down'),
    name="Bottoms",
    hoverinfo='text',
    text=[f"Bottom<br>Date: {data.index[i].strftime('%Y-%m-%d %H:%M')}<br>Price: {p:.2f}" for i, p in bottoms]
))

# Customize layout
fig.update_layout(
    title="Interactive Nifty Close Price with Local Tops & Bottoms",
    xaxis_title="Date",
    yaxis_title="Price",
    hovermode="x unified",
    template="plotly_dark"
)

# Show interactive chart
fig.show()
