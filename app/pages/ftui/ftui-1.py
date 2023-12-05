from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

df = pd.DataFrame(dict(
    r=[0, 0, 0, 0, 0],
    skills=["skill a", "skill b", "skill c", "skill d", "skill e"]))

fig = px.line_polar(df, r='r', theta='skills', line_close=True)

register_page(__name__)

layout = html.Div([
    dbc.Card(
        dbc.CardBody(
            [
                html.H2("What fields are you interested in?"),
                html.Div(
                    dcc.Dropdown(
                        [
                            "Technology",
                            "Healthcare",
                            "Finance",
                            "Education",
                        ],
                        multi=True,
                        style={"width": "100%"}
                    ),
                    style={"width": "50%"}
                ),
            ],
            style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column"}
        ),
        style={"marginTop": "2vh"}
    ),
    dbc.Card(
        dbc.CardBody(
            [
                html.H2("What jobs are you interested in?"),
                html.Div(
                    dcc.Dropdown(
                        [
                            "Software Developer",
                            "Data Scientist",
                            "Network Engineer",
                            "Cybersecurity Analyst",
                            "UI/UX Designer",
                            "Hardware Engineer",
                            "System Administrator",
                            "IT Support Specialist"
                        ],
                        style={"width": "100%"}
                    ),
                    style={"width": "50%"}
                ),
            ],
            style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column"}
        ),
        style={"marginTop": "2vh"}
    ), 
    dbc.Card(
        dbc.CardBody(
            [
                html.P("Let's see how your skills do with a baseline quiz."),
                html.A(dbc.Button("Let's go!", color="primary", className="mr-1"), href="/ftui/ftui-2"),
            ],
            style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column"}
        ),
        style={"marginTop": "2vh"}
    ), 
])