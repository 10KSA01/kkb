from dash import html, dcc
import dash_bootstrap_components as dbc

def create_navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Shop", href="/shop")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Profile", href="#"),
                    dbc.DropdownMenuItem("Settings", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="Profile",
            ),
        ],
        brand="Quizi",
        brand_href="/",
        color="primary",
        dark=True,
        fluid=True,
        style={"padding": "0.5vh 2vw"}
    )