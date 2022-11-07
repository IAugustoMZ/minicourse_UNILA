import os
import json
from app import *
import numpy as np
import pandas as pd
from globals import *
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# load dictionary to create limits of the inputs
DATASOURCE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'data', '3_model_data', 'tag_limits.json')

with open(DATASOURCE, 'r') as file:
    limits = json.load(file)
    file.close()

# set sidebar layout
layout = dbc.Col([
    html.H1('Predictive Maintenance Panel', className='text_primary'),
    html.P('by UNILA students', className='text-info'),
    html.Hr(),

    # logo section
    dbc.Button(id='botao_logo',
    children=[
        html.Img(src='assets/imgs/logo_unila.png', id='logo_change', alt='UNILA', className='logo_unila'),
        html.Img(src='assets/imgs/logo_flaeq.png', id='logo_flaeq', alt='FLAEQ', className='logo_flaeq')
    ],
    style={'background-color': 'transparent', 'border-color': 'transparent'},
    class_name='perfil_avatar'),

    # add sensor data inputs
    dbc.Row([
        dbc.Col([
            dbc.Label('Plant Runtime (cycles)'),
            dbc.Input(placeholder='no of cycles', id='text-cycles')
        ], width=6),
        dbc.Col([
            dbc.Button('Send Data', color='success', id='send_data')
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label('Tag 2: '),
            dcc.Slider(round(limits['tag2']['min'], 1), round(limits['tag2']['max'], 1), 0.1,
                       marks={
                        round(limits['tag2']['min'], 1): str(round(limits['tag2']['min'], 1)),
                        round(limits['tag2']['max'], 1): str(round(limits['tag2']['max'], 1))},
                       tooltip={'placement': 'bottom', 'always_visible': False},
                       id='tag2')
        ], width=6),
        dbc.Col([
            dbc.Label('Tag 3: '),
            dcc.Slider(round(limits['tag3']['min'], 1), round(limits['tag3']['max'], 1), 0.1,
                       marks={
                        round(limits['tag3']['min'], 1): str(round(limits['tag3']['min'], 1)),
                        round(limits['tag3']['max'], 1): str(round(limits['tag3']['max'], 1))},
                       tooltip={'placement': 'bottom', 'always_visible': False},
                       id='tag3')
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label('Tag 4: '),
            dcc.Slider(round(limits['tag4']['min'], 1), round(limits['tag4']['max'], 1), 0.1,
                       marks={
                        round(limits['tag4']['min'], 1): str(round(limits['tag4']['min'], 1)),
                        round(limits['tag4']['max'], 1): str(round(limits['tag4']['max'], 1))},
                       tooltip={'placement': 'bottom', 'always_visible': False},
                       id='tag4')
        ], width=6),
        dbc.Col([
            dbc.Label('Tag 7: '),
            dcc.Slider(round(limits['tag7']['min'], 1), round(limits['tag7']['max'], 1), 0.1,
                       marks={
                        round(limits['tag7']['min'], 1): str(round(limits['tag7']['min'], 1)),
                        round(limits['tag7']['max'], 1): str(round(limits['tag7']['max'], 1))},
                       tooltip={'placement': 'bottom', 'always_visible': False},
                       id='tag7')
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label('Tag 9: '),
            dcc.Slider(round(limits['tag9']['min'], 1), round(limits['tag9']['max'], 1), 0.1,
                       marks={
                        round(limits['tag9']['min'], 1): str(round(limits['tag9']['min'], 1)),
                        round(limits['tag9']['max'], 1): str(round(limits['tag9']['max'], 1))},
                       tooltip={'placement': 'bottom', 'always_visible': False},
                       id='tag9')
        ], width=6),
        dbc.Col([
            dbc.Label('Tag 11: '),
            dcc.Slider(round(limits['tag11']['min'], 1), round(limits['tag11']['max'], 1), 0.1,
                       marks={
                        round(limits['tag11']['min'], 1): str(round(limits['tag11']['min'], 1)),
                        round(limits['tag11']['max'], 1): str(round(limits['tag11']['max'], 1))},
                       tooltip={'placement': 'bottom', 'always_visible': False},
                       id='tag11')
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label('Tag 12: '),
            dcc.Slider(round(limits['tag12']['min'], 1), round(limits['tag12']['max'], 1), 0.1,
                       marks={
                        round(limits['tag12']['min'], 1): str(round(limits['tag12']['min'], 1)),
                        round(limits['tag12']['max'], 1): str(round(limits['tag12']['max'], 1))},
                       tooltip={'placement': 'bottom', 'always_visible': False},
                       id='tag12')
        ], width=6),
        dbc.Col([
            dbc.Label('Tag 14: '),
            dcc.Slider(round(limits['tag14']['min'], 1), round(limits['tag14']['max'], 1), 0.1,
                       marks={
                        round(limits['tag14']['min'], 1): str(round(limits['tag14']['min'], 1)),
                        round(limits['tag14']['max'], 1): str(round(limits['tag14']['max'], 1))},
                       tooltip={'placement': 'bottom', 'always_visible': False},
                       id='tag14')
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label('Tag 15: '),
            dcc.Slider(round(limits['tag15']['min'], 1), round(limits['tag15']['max'], 1), 0.1,
                       marks={
                        round(limits['tag15']['min'], 1): str(round(limits['tag15']['min'], 1)),
                        round(limits['tag15']['max'], 1): str(round(limits['tag15']['max'], 1))},
                       tooltip={'placement': 'bottom', 'always_visible': False},
                       id='tag15')
        ], width=6),
        dbc.Col([
            dbc.Label('Tag 17: '),
            dcc.Slider(round(limits['tag17']['min'], 1), round(limits['tag17']['max'], 1), 0.1,
                       marks={
                        round(limits['tag17']['min'], 1): str(round(limits['tag17']['min'], 1)),
                        round(limits['tag17']['max'], 1): str(round(limits['tag17']['max'], 1))},
                       tooltip={'placement': 'bottom', 'always_visible': False},
                       id='tag17')
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label('Tag 20: '),
            dcc.Slider(round(limits['tag20']['min'], 1), round(limits['tag20']['max'], 1), 0.1,
                       marks={
                        round(limits['tag20']['min'], 1): str(round(limits['tag20']['min'], 1)),
                        round(limits['tag20']['max'], 1): str(round(limits['tag20']['max'], 1))},
                       tooltip={'placement': 'bottom', 'always_visible': False},
                       id='tag20')
        ], width=6),
        dbc.Col([
            dbc.Label('Tag 21: '),
            dcc.Slider(round(limits['tag21']['min'], 1), round(limits['tag21']['max'], 1), 0.1,
                       marks={
                        round(limits['tag21']['min'], 1): str(round(limits['tag21']['min'], 1)),
                        round(limits['tag21']['max'], 1): str(round(limits['tag21']['max'], 1))},
                       tooltip={'placement': 'bottom', 'always_visible': False},
                       id='tag21')
        ], width=6)
    ])
], id='sidebar_complete')

# callbacks ----------------------------------------------------------------------------------------------
@app.callback(
    Output('store-predictions', 'data'),
    Input('send_data', 'n_clicks'),
    [
        State('text-cycles', 'value'),
        State('tag2', 'value'),
        State('tag3', 'value'),
        State('tag4', 'value'),
        State('tag7', 'value'),
        State('tag9', 'value'),
        State('tag11', 'value'),
        State('tag12', 'value'),
        State('tag14', 'value'),
        State('tag15', 'value'),
        State('tag17', 'value'),
        State('tag20', 'value'),
        State('tag21', 'value'),
        State('store-predictions', 'data')
    ]
)
def update_data_predictions(n,
                            runtime,
                            tag2, tag3,
                            tag4, tag7,
                            tag9, tag11,
                            tag12, tag14,
                            tag15, tag17,
                            tag20, tag21,
                            predictions_dict):

    # transform the data in dictionary to data frame
    predictions_data = pd.DataFrame(predictions_dict)

    # deal with missing values
    if not runtime:
        runtime = 0.0

    if not tag2:
        tag2 = limits['tag2']['min'] 

    if not tag3:
        tag3 = limits['tag3']['min'] 

    if not tag4:
        tag4 = limits['tag4']['min'] 

    if not tag7:
        tag7 = limits['tag7']['min'] 

    if not tag9:
        tag9 = limits['tag9']['min'] 

    if not tag11:
        tag11 = limits['tag11']['min']

    if not tag12:
        tag12 = limits['tag12']['min']

    if not tag14:
        tag14 = limits['tag14']['min']

    if not tag15:
        tag15 = limits['tag15']['min']

    if not tag17:
        tag17 = limits['tag17']['min']

    if not tag20:
        tag20 = limits['tag20']['min']

    if not tag21:
        tag21 = limits['tag21']['min']

    # transform sensor data into list
    input_list = [
        float(runtime), tag2, tag3, tag4, tag7,
        tag9, tag11, tag12, tag14, tag15, 
        tag17, tag20, tag21
    ]

    # create an array with the inputs list
    input_to_model = np.array(input_list).reshape(1, -1)
    
    # make the predictions
    rul = regression_model.predict(input_to_model)
    prob = classification_model.predict_proba(input_to_model)

    # append results of predictions in the input list
    input_list.append(rul[0])
    input_list.append(prob[0][1])

    # update the dataframe after the click
    if (n and (None not in input_list)):

        # update dataset
        predictions_data.loc[predictions_data.shape[0]] = input_list

        # save dataset
        predictions_data.to_csv(os.path.join(DASHBOARD_PATH, 'predictions.csv'), index=False)

    return predictions_data.to_dict()