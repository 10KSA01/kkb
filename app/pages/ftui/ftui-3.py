from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

df = pd.DataFrame(dict(
    r=[0, 2, 1, 4, 0, 7, 2],
    skills=["Languages", "Mathematics and Science", "Social Studies", "Creative Arts", "Technology",
            "Religious and Ethical Education", "Business and Economics"]))

fig = px.line_polar(df, r='r', theta='skills', line_close=True)

register_page(__name__)

layout = dbc.Card([
    dbc.CardBody(
        [
            html.P("Here are your skills:"),
            dcc.Graph(figure=fig),
        ],
        style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column"}
    ),

    html.Div(
        style={"display": "flex", "justify-content": "center", "align-items": "center", "flex-direction": "column"},
        children = [
            html.A(dbc.Button("Start taking quizzes", color="success", style={"width": "100%"}),
                href="/quizselection", style={"display": "flex", "width": "90%", "margin": "2vh 2vw"})
        ]
    )

])