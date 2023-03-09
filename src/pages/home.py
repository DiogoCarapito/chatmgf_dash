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
        dbc.Col(html.Div(), width=2),

        dbc.Col(
            html.Div([

                dbc.Row([
                    dbc.Container([
                        html.P(id="output"),
                    ],style={"height": "400px"}),
                ]),

                dbc.Row([
                    dbc.Col([
                        dbc.Input(id="input", placeholder="Pergunta-me algo", type="text"),
                    ], width=10),
                    dbc.Col([
                        dbc.Button("Enviar...", color="info", className="me-1", id="send"),
                    ], width=2)
                ]),

            ], className="h-100")
        ),

        dbc.Col(html.Div(), width=2),
    ]),

], fluid=True)


def layout():
    return html.Div([
        container,
        html.Br(),
    ])

@callback(
    Output('output', 'children'),
    Input('send', 'n_clicks'),
    Input('input', 'value'),

)

def prompt(n_clicks, input):
    if n_clicks == 0:
        return html.P("")
    else:
        n_clicks = 0
        return html.P(input)

