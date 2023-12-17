import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = dbc.Container([
    html.H1("Contact Us", className="display-4"),

    # Add a contact form or information
], style={'padding': '20px'})
