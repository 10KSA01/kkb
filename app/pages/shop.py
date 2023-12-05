from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
from components.Items import example_shop_item


register_page(__name__)

layout = dbc.CardBody(
    [
        dbc.Row([
            dbc.Col(
                [
                    html.H2("Welcome to the Shop"),
                    html.P("Explore our collection of items and make your purchase."),
                ],
                width=12, className="text-center"
            ),
        ]),
        html.Br(),
        dbc.Row(
            [
                dbc.Col([example_shop_item("item 1 $5")], width=3),
                dbc.Col([example_shop_item("item 2 $3")], width=3),
                dbc.Col([example_shop_item("item 3 $10")], width=3),
                dbc.Col([example_shop_item("item 4 $100")], width=3),
            ],
            align="center",
        ),
        html.Br(),
    ]
)