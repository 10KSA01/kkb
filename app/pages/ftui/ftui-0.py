from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

df = pd.DataFrame(dict(
    r=[0, 0, 0, 0, 0],
    skills=["skill a", "skill b", "skill c", "skill d", "skill e"]))

fig = px.line_polar(df, r='r', theta='skills', line_close=True)

register_page(__name__)

layout = dbc.Card(
    dbc.CardBody(
        [
            html.H1("Welcome Dave!"),
            html.P("Let's get started. This is you:"),
            html.Img(src="/assets/images/profile-pic.jpg", style={"width": "10%"}),
            html.P("Newbie", style={"color": "#aaa", "marginTop": "-1vh"}),
            dcc.Graph(figure=fig),
            html.P("It's time to get know you. Are you ready?"),
            html.A(dbc.Button("Let's go!", color="primary", className="mr-1"), href="/ftui/ftui-1"),
        ],
        style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column"}
    ),
)