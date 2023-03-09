import dash
from dash import Dash, dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc


dash.register_page(
    __name__,
    path='/',
    title='ChatMGF',
    name='Chat',
    order=1,
)

container = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div(), width=3),
        dbc.Col(
            dbc.Container([
                dbc.Row([
                    html.P(id="output"),
                ]),
                dbc.Row([
                    dbc.Input(id="input", placeholder="Pergunta-me algo", type="text"),
                ]),
            ],
        )),
        dbc.Col(html.Div(), width=3),
    ]),

], fluid=True)


def layout():
    return html.Div([
        container,
        html.Br(),
    ])

@callback(
    Output('output', 'children'),
    Input('input', 'value'),
)

def prompt(input):
    return html.P(input)