import dash
# Code from: https://github.com/plotly/dash-labs/tree/main/docs/demos/multi_page_example1
dash.register_page(__name__)

from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc


layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            html.H1("Welcome to Analytix Edge", className="display-3"),
            width={"size": 6, "offset": 3}
        ),
    ),
    dbc.Row(
        dbc.Col(
            html.Div([
                html.P(
                    """
                    At Analytix Edge, we're at the forefront of data science and analytics, helping businesses unlock the hidden potential of their data. Our expertise lies in two key areas: machine learning and dashboard building.
                    """,
                    className="lead",
                ),
                html.P(
                    """
                    What sets us apart is our unique approach to data collection. We specialize in web scraping, a powerful technique that enables us to extract valuable information from the vast world of online data. This means you can eliminate blind spots and gain critical insights that traditional data sources might miss.
                    """,
                ),
                html.P(
                    """
                    Here are a few examples of how Analytix Edge can benefit your business:
                    """,
                    className="lead",
                ),
                html.Ul([
                    html.Li("Market Analysis: We can scrape competitor websites to gather pricing and product data for informed pricing strategies."),
                    html.Li("Lead Generation: Our web scraping techniques can identify potential leads and contacts for your sales team."),
                    html.Li("Competitive Intelligence: Track market trends, consumer sentiment, and competitor activities by collecting data from various sources."),
                ]),
            ],
                style={
                    "text-align": "justify",
                    "margin-left": "20%",
                    "margin-right": "5%",
                }
            ),
            width={"size": 10}
        ),
    ),
], fluid=True)
