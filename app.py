import dash
from dash import Input, Output, State, html
from dash import dcc
import dash_bootstrap_components as dbc

import requests

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1('Hello, World!!'),
])


if __name__ == '__main__':
    app.run(debug=True)