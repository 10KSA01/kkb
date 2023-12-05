# page to be used during a quiz
import dash
from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


register_page(__name__)


answers = ["Went", "Goed", "Gone", "Going"]
correct = "A"

buttons = [
    dbc.Row([
        dbc.Card([
            html.Div([
                html.H3(f"{answer}"),
            ],
                id=f"quizbutton-{n+1}"
            ),

        ])
    ])
    for n, answer in enumerate(answers)


]



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
    ],
        className="m-2",
    ),

    dbc.Row([
        dbc.Card([
            html.H4("timer progress bar if possible"),
        ])
    ],
        className="m-2",
    ),

    dbc.Row([

        dbc.Card([
            html.H1("THIS IS WHERE THE QUESTION GOES"),
            html.H3("Here is some question context or description")

        ])
    ],
        className="m-2",
    ),


    dbc.Row([
        # First Column in the second row
        dbc.Col([
            buttons[0],
            buttons[2]
        ],
            width=6,
        ),

        dbc.Col([

            buttons[1],
            buttons[3]

        ],
            width=6,
        ),


    ]),
])


@dash.callback(
    Output("quizbutton-1", "n_clicks_timestamp"),
    [Input("quizbutton-1", "n_clicks_timestamp"),
    Input("quizbutton-2", "n_clicks_timestamp"),
    Input("quizbutton-3", "n_clicks_timestamp"),
    Input("quizbutton-4", "n_clicks_timestamp")],
)
def add_score_callback(b1, b2, b3, b4):
    # defaults to -1, max is most recent

    bs = [(n if n is not None else -1) for n in [b1, b2, b3, b4]]
    m = max(bs)
    mInd = max(enumerate(bs), key=lambda x: x[1])[0]
    print(bs, m, mInd)
    if m > -1:
        print("ABCD"[mInd])
        if "ABCD"[mInd] == correct:
            #TODO add 1 to current score
            pass
        #TODO add 1 to qs complete
        #TODO: change to new page

    return b1


