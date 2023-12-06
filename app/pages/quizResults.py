from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc


register_page(__name__)



stars = 3
stars_unicode = "".join(["★"] * stars + ["☆"] * (3-stars))

# Use the Dash app with a Bootstrap theme

layout = dbc.Container([
    # First Row
    dbc.Row([
        dbc.Col(
            dbc.Card([
                html.H3("Quiz title"),
            ]),
            width=6  # This column takes half of the row
        ),
        dbc.Col(
            dbc.Card([
                html.H3(f"Difficulty: {stars_unicode}"),
            ]),
            width=4
        ),

        dbc.Col(
            dbc.Card([
                dbc.Button([
                    html.H3("Next Quiz")
                ], color="primary", style={"width": "100%"}, href="/quizstart"),
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
                html.H2("Level "),
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
                html.H2("+27 XP")
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


