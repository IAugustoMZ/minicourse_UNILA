from app import *
import numpy as np
import pandas as pd
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# set graph margin
graph_margin=dict(l=25, r=25, t=25, b=0)

# set dashboard layout
layout = dbc.Col([
    # predicted KPI
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Legend('Remaining Useful Life'),
                html.H6('-', id='p-rul', style={})
            ], style={'padding-left': '20px', 'padding-top': '10px'})
        ], width=6),
        dbc.Col([
            dbc.Card([
                html.Legend('Probability of Failure'),
                html.H6('-', id='p-prob', style={})
            ], style={'padding-left': '20px', 'padding-top': '10px'})
        ], width=6)
    ], style={'margin': '0.5px'}),
    # plot the evolution of RUL prediction
    dbc.Col(
        dbc.Card(dcc.Graph(id='rul_history'), style={'height': '100%', 'padding': '10px', 'margin': '10px'}),
        width=12
    ),
    # plot the evolution of probability of failure prediction
    dbc.Col(
        dbc.Card(dcc.Graph(id='prob_history'), style={'height': '100%', 'padding': '10px', 'margin': '10px'}),
        width=12
    ),
])

# function callbacks -------------------------------------------------------------------------------------------------
# update RUL prediction
@app.callback(
    Output('p-rul', 'children'),
    [
        Input('send_data', 'n_clicks'),
        Input('store-predictions', 'data')
    ]
)
def predicted_rul(n, data) -> str:

    # transform data back to dataframe
    pred = pd.DataFrame(data)

    # after the click, take the last predicted RUL
    if n:
        pred_rul = pred.tail(1)['rul_pred'].values[0]
    else:
        pred_rul = 0

    # create text to return
    text = f'RUL = {int(pred_rul)} cycles (+- 40 cycles)'

    return text

# update probability of failure
@app.callback(
    Output('p-prob', 'children'),
    [
        Input('send_data', 'n_clicks'),
        Input('store-predictions', 'data')
    ]
)
def predicted_rul(n, data) -> str:

    # transform data back to dataframe
    pred = pd.DataFrame(data)

    # after the click, take the last predicted RUL
    if n:
        pred_prob = pred.tail(1)['prob_pred'].values[0]
    else:
        pred_prob = 0

    # create text to return
    text = f'P = {round(pred_prob * 100, 2)} % (in the next 50 cycles)'

    return text

# update RUL history plot
@app.callback(
    Output('rul_history', 'figure'),
    [
        Input('store-predictions', 'data')
    ]
)
def update_rul_history_plot(data):

    # transform data back to dataframe
    pred = pd.DataFrame(data)

    # build plot
    fig = go.Figure()

    fig.add_trace(
        go.Line(name='Predicted RUL', 
        x = list(range(pred.shape[0])),
        y = pred['rul_pred']))

    fig.add_shape(
        type='line',
        x0=0,
        y0=50,
        x1=pred.shape[0]-1,
        y1=50,
        line=dict(
            color='red',
            dash='dash',
            width=2
        )
    )
    fig.update_layout(margin=graph_margin)
    fig.update_yaxes(title_text='RUL Prediction')
    fig.update_xaxes(title_text='# Executions')

    return fig

# update probability history plot
@app.callback(
    Output('prob_history', 'figure'),
    [
        Input('store-predictions', 'data')
    ]
)
def update_rul_history_plot(data):

    # transform data back to dataframe
    pred = pd.DataFrame(data)

    # build plot
    fig = go.Figure()

    fig.add_trace(
        go.Line(name='Probability of Failure', 
        x = list(range(pred.shape[0])),
        y = pred['prob_pred']))
    fig.add_shape(
        type='line',
        x0=0,
        y0=0.01,
        x1=pred.shape[0]-1,
        y1=0.01,
        line=dict(
            color='yellow',
            dash='dash',
            width=2
        )
    )
    fig.add_shape(
        type='line',
        x0=0,
        y0=0.05,
        x1=pred.shape[0]-1,
        y1=0.05,
        line=dict(
            color='orange',
            dash='dash',
            width=2
        )
    )
    fig.add_shape(
        type='line',
        x0=0,
        y0=0.1,
        x1=pred.shape[0]-1,
        y1=0.1,
        line=dict(
            color='red',
            dash='dash',
            width=2
        )
    )
    fig.update_layout(margin=graph_margin)
    fig.update_yaxes(title_text='Prediction of Probability of Failure')
    fig.update_xaxes(title_text='# Executions')

    return fig