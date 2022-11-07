from app import *
import numpy as np
import pandas as pd
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

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
    ], style={'margin': '10px'}),
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