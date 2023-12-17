import dash_bootstrap_components as dbc
from dash import html

def create_sidebar():
    sidebar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("Services", href="/services")),
            dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
        ],
        brand="AnalytixEdge",
        brand_href="/",
        color="dark",
        dark=True,
        id='navbar'
    )

    return html.Div([sidebar])

