from app import *
from globals import *
from dash import html, dcc
import dash_bootstrap_components as dbc
from components import sidebar, dashboards
from dash.dependencies import Input, Output

# create layout
content = html.Div(id='page-content')

# set layout to app
app.layout = dbc.Container(children=[

    # create stores for store input data
    dcc.Store(id='store-predictions', data=data.to_dict()),

    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md=4),
        dbc.Col([
            content
        ], md=8)
    ])
], fluid=True, style={'padding': '10px'}, className='dbc')

# callbacks functions
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname: str)-> object:
    """
    renders the page according to the inputted
    url

    Parameters
    ----------
    pathname : str
       page pathname

    Returns
    -------
    object
       page layout
    """
    return dashboards.layout

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)