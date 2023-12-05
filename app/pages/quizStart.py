from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
from components.MiniStats import *
from components.Tables import example_quest_score
import random
import pandas as pd
import plotly.express as px
import platform
import json
register_page(__name__)

file_path = "app/data/skills.json" if platform.system() == 'Windows' else "data/skills.json"

with open(file_path, 'r') as file:
    skills_data = json.load(file)

skills_list = list(skills_data['MainSkills'].keys())

skill_levels = []
dream_job_skill_levels = []
for skill in skills_data['MainSkills']:
    skill_levels.append(random.randint(0, 10))
    dream_job_skill_levels.append(random.randint(10, 20))

df1 = pd.DataFrame(dict(
    level=skill_levels,
    skills=skills_list,
))

df2 = pd.DataFrame(dict(
    level=dream_job_skill_levels,
    skills=skills_list,
))

df1['Type'] = 'You'
df2['Type'] = 'Software Engineer'

df = pd.concat([df1, df2], ignore_index=True)

fig = px.line_polar(df, r='level', theta='skills', color="Type", line_close=True)

description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# Use the Dash app with a Bootstrap theme
layout = dbc.CardBody(
    [
        html.Br(),
        dbc.Row([
            dbc.Col(html.H1("Quiz title"), width={"offset": 1}),
            dbc.Col(dbc.Button("Start", href="/quizquestion"),width={"offset": 6})
        ]),
        html.Br(),
        dbc.Row(dbc.Col(html.H3("Quiz description"), width={"offset": 1})),
        dbc.Row([
            dbc.Col(html.P(description), width={"offset": 1, "size": 6}),
            dbc.Col(mini_stat("bi bi-clock", "3 Min")),
            dbc.Col(mini_stat("bi bi-arrow-up", "+27 XP")),
            dbc.Col(mini_stat("bi bi-star-fill", "Hard")),
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col(example_quest_score(), width={"offset": 1, "size": 5}),
            dbc.Col([
                html.Div(
                    dcc.Graph(
                        figure=fig,
                        style={'width': '100%'}
                    )
                )
                ], width={"size": 6}),

        ])
    ]
)
# layout = dbc.Container([
#     # First Row
#     dbc.Row([
#         # First Column in the first row
#         dbc.Col(
#             dbc.Card([
#                 html.H3("Quiz title"),
#             ]),
#             width=6  # This column takes half of the row
#         ),

#         # Second Column in the first row
#         dbc.Col(
#             dbc.Card([
#                 html.H3("Difficulty in stars"),
#             ]),
#             width=4
#         ),

#         dbc.Col(
#             dbc.Card([
#                 dbc.NavItem(dbc.NavLink("START QUIZ", href="/quizquestion")),
#             ]),
#             width=2 # last 2/12ths of a row
#         ),
#     ],
#     className="m-2",
#     ),

#     # Second Row
#     dbc.Row([
#         # First Column in the second row
#         dbc.Col([

#                 dbc.Row([

#                     dbc.Card([
#                         html.H3("Quiz description"),
#                         html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
#                     ]),
#                 ]),

#                 dbc.Row([

#                     dbc.Card([
#                         html.H3("Time limit"),
#                         html.P("PUT A PROGRESS BAR HERE"),
#                     ]),
#                 ]),

#                 dbc.Row([

#                     dbc.Card([
#                         html.H3("Quiz XP"),
#                         html.P("PUT AN XP BAR HERE"),
#                     ]),
#                 ]),
#             ],



#             width=6,
#         ),

#         # Second Column in the second row
#         dbc.Col([
#             dbc.Row([

#                 dbc.Card([
#                     html.H3("Prev score"),
#                     html.P("Score as % or 'First attempt, give it a go!'"),
#                 ]),
#             ]),

#             dbc.Row([

#                 dbc.Card([
#                     html.H3("Friend high score section"),
#                     html.P("Friend high score thingy"),
#                 ]),
#             ]),

#             dbc.Row([

#                 dbc.Card([
#                     html.H3("Skill radar graph"),
#                     html.P("Skill radar graph"),
#                 ]),
#             ]),


#         ],
#             width=6
#         ),
#     ],

#     className="m-3"
#     ),
# ])


