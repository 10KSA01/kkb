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
                dbc.NavItem(dbc.NavLink("START QUIZ", href="/quizquestion")),
            ]),
            width=2 # last 2/12ths of a row
        ),
    ],
        className="m-2",
    ),

    # level up bar row
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H2("Level bar, shows progress in different colour")
            ])
        ], width=9),

        dbc.Col([
            dbc.Card([
                html.H2("+n XP")
            ])
        ], width=3),
    ],
        className="m-2",
    ),

    # Second Row
    dbc.Row([
        # First Column in the second row
        dbc.Col([

            dbc.Row([
                dbc.Card([
                    html.H1("SCORE!")
                ]),
            ]),

            dbc.Row([

                dbc.Card([
                    html.H3("Quiz breakdown"),
                ]),
            ]),
        ],
            width=6,
        ),

        # Second Column in the second row
        dbc.Col([
            dbc.Row([

                dbc.Card([
                    html.H3("Prev score"),
                    html.P("Score as % or 'First attempt, give it a go!'"),
                ]),
            ]),

            dbc.Row([

                dbc.Card([
                    html.H3("Friend high score section"),
                    html.P("Friend high score thingy"),
                ]),
            ]),

            dbc.Row([

                dbc.Card([
                    html.H3("Skill radar graph"),
                    html.P("Skill radar graph"),
                ]),
            ]),


        ],
            width=6
        ),
    ],
    className="m-3"
    ),
])


