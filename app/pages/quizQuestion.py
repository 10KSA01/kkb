# page to be used during a quiz

from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc


register_page(__name__)


# Use the Dash app with a Bootstrap theme

layout = dbc.Container([
    # First Row
    dbc.Row([
        # First Column in the first row
        dbc.Col(
            dbc.Card([
                html.H3("Quiz title"),
            ]),
            width=6  # This column takes half of the row
        ),

        # Second Column in the first row
        dbc.Col(
            dbc.Card([
                html.H3("Difficulty in stars"),
            ]),
            width=4
        ),

        dbc.Col(
            dbc.Card([
                html.H3("Progress, either q/tot or as a bar"),
            ]),
            width=2 # last 2/12ths of a row
        ),
    ]),

    dbc.Row([

        dbc.Card([
            html.H1("THIS IS WHERE THE QUESTION GOES"),
            html.H3("Here is some question context or description")

        ])
    ]),


    dbc.Row([
        # First Column in the second row
        dbc.Col([
            dbc.Row([
                dbc.Card([
                    html.H3("Question answer 1"),
                ])
            ]),

            dbc.Row([
                dbc.Card([
                    html.H3("Question answer 3"),
                ])
            ])
        ],
            width=6,
        ),

        dbc.Col([

            dbc.Row([
                dbc.Card([
                    html.H3("Question answer 2"),
                ])
            ]),

            dbc.Row([
                dbc.Card([
                    html.H3("Question answer 4"),
                ])
            ]),

        ],
            width=6,
        ),


    ]),
])


