from dash import html, dcc
import dash_bootstrap_components as dbc

def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Main Page", href="/")),
            dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
            dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
            dbc.NavItem(dbc.NavLink("quiz start broken", href="/quiz_start")),
        ],
        brand="KBB",
        brand_href="/",
        color="primary",
        dark=True,
    )
    return navbar
