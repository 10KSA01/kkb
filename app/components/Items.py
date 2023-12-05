import dash_bootstrap_components as dbc
from dash import html
import platform

placeholder_path = ""
if platform.system() == 'Windows':
    placeholder_path = "/assets/images/placeholder.png"  # Note the leading '/'
else:
    placeholder_path = "/assets/images/placeholder.png"

def example_shop_item(item):
    card = dbc.Card(
        [
            dbc.CardImg(src=placeholder_path, top=True),
            dbc.CardBody(
                [
                    html.H4(item, className="card-title"),
                    dbc.Button("Buy", color="primary", className="mx-auto d-block"),
                ]
            ),
        ],
        className="d-grid mx-auto"
    )
    
    return card
