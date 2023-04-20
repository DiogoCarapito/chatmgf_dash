import dash
from dash import Dash, dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc


dash.register_page(
    __name__,
    path='/',
    title='ChatMGF.com',
    name='Chat',
    order=1,
)

chat = []

chat_card = dbc.Card([
    dbc.CardBody([
        dbc.Row([
            html.Div([
                html.P(id="output"),
            ],style={"height": "500px", "overflow-y": "scroll"}),
        ]),

    ], style={"hight":"500px"}),
    dbc.CardFooter([
        html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.Input(id="input_text", placeholder="Pergunta-me algo", type="text", value=''),
                ], width=10),
                dbc.Col([
                    dbc.Button(color="info", className="me-1, bi bi-send", id="send"),
                ], width=1),
                dbc.Col([
                    dbc.Button(color="primary", className="me-1, bi bi-trash", id="trash"),
                ], width=1),
            ]),
        ]),
    ]),
])

container = dbc.Container([
    html.Br(),

    dbc.Row([
        html.H1('ChatMGF', style={'textAlign': 'center'}),
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col(html.Div(), width=1),
        dbc.Col([chat_card], width=10),
        dbc.Col(html.Div(), width=1),
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
    Input('trash', 'n_clicks'),
    State('input_text', 'value'),
)

def prompt(send, trash, input):
    if trash is not None:
        trash = 0
        input = None
        return ''
    if send is not None:
        chat.append(html.Div(html.P(input)))
        send = 0
        return chat
