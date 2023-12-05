from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
from components.Charts import *
from components.Tables import *
from components.MiniCards import *


register_page(__name__, path='/')

layout = dbc.CardBody(
    [
        dbc.Row(
            [
                dbc.Col([example_radar_chart()], width=6),
                dbc.Col([example_activity_friends()], width=6),
            ],
            align="center",
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col([example_daily_quest()], width=6),
                dbc.Col([
                    dbc.Row([example_card("Recommended Field", "Computer Science")]),
                    html.Br(),
                    dbc.Row([example_card("Recommended Job", "Software Engineer")]),
                ], width=6)
                
            ],
            align="center"
        ),
        html.Br(),
    ]
)