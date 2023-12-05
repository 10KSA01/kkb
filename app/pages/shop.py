from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
from components.Items import example_shop_item


register_page(__name__)

layout = dbc.CardBody(
    [
        html.Br(),
        dbc.Row([
            dbc.Col(
                [
                    html.H2("Welcome to the Shop"),
                    html.P("Explore our collection of accessories and make your purchase."),
                ],
                width=12, className="text-center"
            ),
        ]),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col([example_shop_item(f"item {i} ${i * 2}")], width=3)
                                for i in range(1, 9)  # Adjust the range based on the number of items
                            ],
                            className="overflow-auto",  # Enable horizontal scrolling
                            style={"flex-wrap": "nowrap"},  # Prevent items from wrapping to the next line
                        ),
                    ],
                    width=11,
                    align="center",
                    style={
                        "display": "flex", 
                        "justify-content": "center", 
                        "align-items": "center", 
                    }
                ),
            ]
        ),
        html.Br(),
    ]
)