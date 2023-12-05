from dash import Dash, html, page_container
import dash_bootstrap_components as dbc
from components.navbar import create_navbar

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], use_pages=True)

app.title = 'KKB'

navbar = create_navbar()

app.layout = html.Div(
    [
        dbc.Row(
            [
                navbar,
                dbc.Row(page_container, style={"display": "flex", "justify-content": "space-evenly", "align-items": "center"}),
            ],
            class_name="g-0"
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, port=8075)