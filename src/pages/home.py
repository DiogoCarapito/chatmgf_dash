import dash
from dash import Dash, dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc


dash.register_page(
    __name__,
    path='/',
    title='ChatMGF',
    name='',
    order=1,
)

container = dbc.Container([
    html.H3('home'),
], fluid=True)


def layout():
    return html.Div([
        container,
        html.Br(),
    ])