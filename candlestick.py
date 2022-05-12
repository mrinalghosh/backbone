# Derived from Plotly Dash tutorial

from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Apple stock candlestick chart'),
    dcc.Checklist(
        id='toggle-rangeslider',
        options=[{'label': 'Include Rangeslider',
                  'value': 'slider'}],
        value=['slider']
    ),
    dcc.Graph(id="graph"),
])


@app.callback(Output("graph", "figure"), Input("toggle-rangeslider", "value"))
def display_candlestick(value):
    # replace with your own data source
    df = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    fig = go.Figure(go.Candlestick(
        x=df['Date'],
        open=df['AAPL.Open'],
        high=df['AAPL.High'],
        low=df['AAPL.Low'],
        close=df['AAPL.Close']
    ))

    layout = go.Layout(
        # TODO: tweak background and paper colors
        paper_bgcolor='rgba(0,0,0,0.5)',
        plot_bgcolor='rgba(0,0,0,0.5)',
        xaxis_rangeslider_visible='slider' in value
    )

    fig.update_layout(layout)

    return fig


app.run_server(debug=True)
