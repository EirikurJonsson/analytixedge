import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = dbc.Container([
    html.H1("Our Services", className="display-4"),

    # Add information about your data science services
], style={'padding': '20px'})


