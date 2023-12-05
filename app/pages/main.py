from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path='/')

layout = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                dbc.Breadcrumb(
                    items=[
                        {"label": "Site 1", "active": True},
                        {"label": "Main Dashboard", "active": True},
                    ],
                )
            ),
        ]
    )
)