from dash import Dash, dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

# Sample data for DataTables
recent_quest = {'': ['Completed Quest: Addition Level 3 (7/10)', 'Completed Quest: Subtraction Level 2 (8/10)', 'Completed Quest: Addition Level 1 (10/10)']}
friend_quest = {'': ['John Completed Quest: Addition Level 3 (5/10)', 'Alice Completed Quest: Subtraction Level 3 (10/10)', 'Bob Completed Quest: Addition Level 3 (1/10)']}
daily_quest = {'': ['New Quest: Addition Level 4', 'New Quest: Subtraction Level 3', 'New Quest: Multiplication Level 1']}


df_recent_quest = pd.DataFrame(recent_quest)
df_friend_quest = pd.DataFrame(friend_quest)
df_daily_quest = pd.DataFrame(daily_quest)

def example_activity_friends():
    activity_table = html.Div(
        [
            dbc.Card([
                dbc.Tabs([
                    dbc.Tab(label='Recent Activity', children=[
                        html.Div([
                            dash_table.DataTable(
                                id='table-1',
                                columns=[{'name': col, 'id': col} for col in df_recent_quest.columns],
                                data=df_recent_quest.to_dict('records'),
                                style_table={'height': '410px'},
                                style_cell={'textAlign': 'left'}
                            ),
                        ]),
                    ]),
                    dbc.Tab(label='Friends Activity', children=[
                        html.Div([
                            dash_table.DataTable(
                                id='table-2',
                                columns=[{'name': col, 'id': col} for col in df_friend_quest.columns],
                                data=df_friend_quest.to_dict('records'),
                                style_table={'height': '410px'},
                                style_cell={'textAlign': 'left'}
                            ),
                        ]),
                    ]),
                ]),
            ]),
        ]
    )
    
    return activity_table

def example_daily_quest():
    daily_table = html.Div(
        [
            dbc.Card([
                dbc.CardHeader("Daily Quest"),
                dash_table.DataTable(
                    id='table-3',
                    columns=[{'name': col, 'id': col} for col in df_daily_quest.columns],
                    data=df_daily_quest.to_dict('records'),
                    style_cell={'textAlign': 'left'}
                ),
            ])
        ]
    )
    
    return daily_table