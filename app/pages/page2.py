from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc


register_page(__name__)


# Use the Dash app with a Bootstrap theme
layout = html.Div([
    # First Row
    dbc.Row([
        # First Column in the first row
        dbc.Col(
            html.Div([
                html.H3("Quiz title"),
            ]),
            width=4  # This column takes half of the row
        ),

        # Second Column in the first row
        dbc.Col(
            html.Div([
                html.H3("Difficulty in stars"),
            ]),
            width=4  # This column takes the other half of the row
        ),

        dbc.Col(
            html.Div([
                html.H3("Start button"),
            ]),
            width=4  # This column takes the other half of the row
        ),
    ]),

    # Second Row
    dbc.Row([
        # First Column in the second row
        dbc.Col(
            html.Div([
                html.H3("Column 1, Row 2"),
                html.P("Some content for the first column in the second row."),
            ]),
            width=6
        ),

        # Second Column in the second row
        dbc.Col(
            html.Div([
                html.H3("Column 2, Row 2"),
                html.P("Some content for the second column in the second row."),
            ]),
            width=6
        ),
    ]),
])


