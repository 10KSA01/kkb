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
                dbc.NavItem(dbc.NavLink("NEXT QUIZ", href="/quizquestion")),
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
                html.H2("Level bar, shows progress in different colour"),
                dbc.Progress(
                    [
                        dbc.Progress(value=30, color="warning", bar=True),
                        dbc.Progress(value=15, color="success", bar=True),
                    ]
                )
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

    dbc.Row([
        dbc.Col([

            dbc.Row([
                dbc.Card([
                    html.H1("SCORE!")
                ]),
            ]),

            dbc.Row([

                dbc.Card([
                    html.H3("Quiz breakdown"),
                    html.P("Maybe by question")
                ]),
            ]),

            dbc.Row([

                dbc.Card([
                    dbc.NavItem(dbc.NavLink("next quiz button", href="/quizstart")),
                ]),
            ]),
        ],
            width=6,
        ),

        # Second Column in the second row
        dbc.Col([
            dbc.Row([

                dbc.Card([
                    html.H3("Friend scoreboard"),
                ]),
            ]),
        ],
            width=6
        ),
    ],
        className="m-3"
    ),
])


