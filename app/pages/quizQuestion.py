# page to be used during a quiz
import dash
from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


register_page(__name__)


#TODO: MASSIVE MAKE THIS READ FROM JSON
#  or similar, maybe do object based approach, with each question having
#  a question, answers and a correct value
questionSet = [
    "What is the past tense of the verb 'to go'?",
    "Which of the following is a synonym for 'happy'?",
    "What is the result of 6 multiplied by 9?",
]
answerSet = [
    ["Went", "Goed", "Gone", "Going"],
    ["Sad", "Joyful", "Angry", "Tired"],
    ["15", "42", "54", "63"],
]
correctSet = [
    "A",
    "B",
    "C",
]

pointer = 0

c_answers = 0

#answers = ["Went", "Goed", "Gone", "Going"]
#correct = "A"
q_completed = 0
q_questions = len(questionSet)
stars = 4

stars_unicode = "".join(["★"] * stars + ["☆"] * (5-stars))

buttons = [
        dbc.Row([
            dbc.Card([
                html.Div([
                    html.H3(f"{answer}",
                            id=f"quizbutton-{n+1}-text"),
                ],
                    id=f"quizbutton-{n+1}"
                ),

            ])
        ])
        for n, answer in enumerate(answerSet[pointer])
    ]


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
                html.H3(f"Difficulty: {stars_unicode}"),
            ]),
            width=4
        ),

        dbc.Col(
            dbc.Card([
                html.H3(f"Q: {q_completed + 1} / {q_questions}",
                        id="quizfraction"),
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
            #html.H1(f"{questionSet[pointer]}",
            html.H1(f"Question loading",
                    id="quizquestion"),
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
    [
        Output("quizbutton-1", "n_clicks_timestamp"),
        Output("quizbutton-2", "n_clicks_timestamp"),
        Output("quizbutton-3", "n_clicks_timestamp"),
        Output("quizbutton-4", "n_clicks_timestamp"),
        #Output("url", "pathname"),
        Output("quizquestion", "children"),
        Output("quizfraction", "children"),
        Output("quizbutton-1-text", "children"),
        Output("quizbutton-2-text", "children"),
        Output("quizbutton-3-text", "children"),
        Output("quizbutton-4-text", "children"),
    ],
    [
        Input("quizbutton-1", "n_clicks_timestamp"),
        Input("quizbutton-2", "n_clicks_timestamp"),
        Input("quizbutton-3", "n_clicks_timestamp"),
        Input("quizbutton-4", "n_clicks_timestamp"),
    ],
)
def add_score_callback(b1, b2, b3, b4):
    # defaults to -1, max is most recent

    global q_completed
    global q_questions


    bs = [(n if n is not None else -1) for n in [b1, b2, b3, b4]]
    m = max(bs)
    mInd = max(enumerate(bs), key=lambda x: x[1])[0]
    print(bs, m, mInd)
    # sometimes callbacks just happen, not sure why. This prevents them being processed
    if m > -1:
        print("ABCD"[mInd])
        if "ABCD"[mInd] == correctSet[q_completed]:
            with open("temp/cur_quiz_score.tmp", "r") as f_r:
                cur_score = int(f_r.read())
            with open("temp/cur_quiz_score.tmp", "w") as f_w:
                f_w.write(f"{cur_score + 1}")

        with open("temp/cur_quiz_answered.tmp", "r") as f_r:
            cur_score = int(f_r.read())
        with open("temp/cur_quiz_answered.tmp", "w") as f_w:
            f_w.write(f"{cur_score + 1}")


        q_completed += 1


        if q_completed == q_questions:
            print("STOPSTOPSTOP")

        #TODO: change to new page

    # Reset button click times
    return [-1] * 4 + [questionSet[q_completed], f"Q {q_completed}/{q_questions}"] + answerSet[q_completed]



