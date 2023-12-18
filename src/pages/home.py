import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = dbc.Container(
    [
        html.H1("Welcome to AnaytixEdge", className="display-4"),

        html.P("As the sole data scientist at AnalytixEdge, I bring expertise in delivering high-impact data science solutions tailored to your business needs. "
               "Explore our services and contact us to embark on a data-driven journey."
               ),
        html.P("Being ")
    ],
    style={'padding': '20px'}
)

