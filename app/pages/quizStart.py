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

    # Second Row
    dbc.Row([
        # First Column in the second row
        dbc.Col([



                dbc.Row([

                    dbc.Card([
                        html.H3("Quiz description"),
                        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
                    ]),
                ]),

                dbc.Row([

                    dbc.Card([
                        html.H3("Time limit"),
                        html.P("PUT A PROGRESS BAR HERE"),
                    ]),
                ]),

                dbc.Row([

                    dbc.Card([
                        html.H3("Quiz XP"),
                        html.P("PUT AN XP BAR HERE"),
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


