# Derived from Plotly Dash tutorial

from portfolio import StockData

from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import dash_daq as daq
import yfinance as yf

default_tickers = ['AMD', 'PLTR']
_start = '2020-01-01'
_end = '2022-01-01'

app = Dash(__name__)

stocks = {ticker: StockData(ticker, _start, _end)
          for ticker in default_tickers}

app.layout = html.Div([
    # NOTE: can't set this if none
    html.H4('Apple stock candlestick chart', id='header'),
    daq.ToggleSwitch(id='my-toggle',
                     value=False),
    html.Div(id='my-toggle-output'),
    dcc.Checklist(
        id='toggle-rangeslider',
        options=[{'label': 'Include Rangeslider',
                  'value': 'slider'}],
        value=['slider']
    ),
    dcc.Graph(id="graph"),
    # TODO: grab value - pull using yf API - graph together
    # TODO: graph adj close and pct change - toggle switch
    dcc.Dropdown(
        ['PLTR', 'SPY', 'AMD'],
        default_tickers,
        multi=True,
        id='dropdown'
    ),
    html.P(id='dummy')
])


@app.callback(
    Output('my-toggle-output', 'children'),
    Input('my-toggle', 'value')
)
def update_output(value):
    return 'The switch is {}.'.format(value)


@app.callback(
    Output('dummy', 'children'),
    Input('dropdown', 'value')
)
def update_tickers(values):
    global stocks
    diff = set(stocks.keys()).difference(values)
    for val in diff:
        stocks.pop(val)

    for val in set(stocks.keys()).symmetric_difference(values):
        stocks[val] = StockData(val, _start, _end)

# @app.callback(
#     Output('test-graph', 'figure'),
#     Input('my-toggle', 'value')
# )
# def switch_graph(value):
#     # switch from candlestick to adj-close graph for selected values
#     df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
#     fig =


# def candlestick(ticker):
#     ''' takes SINGLE stock name and returns a candlestick graph '''
#     yf.download()
#     return go.Figure(go.Candlestick)

def multiplot():
    global stocks
    return [go.Scatter(x=v.df.index, y=v.df['Adj Close'], name=k) for (k, v) in stocks.items()]


@app.callback(
    Output("graph", "figure"),
    Input("toggle-rangeslider", "value"),
    Input('my-toggle', 'value'),
    Input('dropdown', 'value')
)
def display_figure(value, toggle, drop):
    # TODO: replace with your own data source
    df = pd.read_csv(
        'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    if toggle:
        graph = go.Candlestick(
            x=df['Date'],
            open=df['AAPL.Open'],
            high=df['AAPL.High'],
            low=df['AAPL.Low'],
            close=df['AAPL.Close']
        )
    else:
        graph = multiplot()

    fig = go.Figure(graph)

    layout = go.Layout(
        # TODO: tweak background and paper colors
        paper_bgcolor='rgba(0,0,0,0.1)',
        plot_bgcolor='rgba(0,0,0,0.1)',
        xaxis_rangeslider_visible='slider' in value
    )

    fig.update_layout(layout)
    return fig


app.run_server(debug=True)
