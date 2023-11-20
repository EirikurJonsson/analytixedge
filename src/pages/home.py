import dash
# Code from: https://github.com/plotly/dash-labs/tree/main/docs/demos/multi_page_example1
dash.register_page(__name__)

from dash import html, Input, Output, callback
import dash_bootstrap_components as dbc

layout = dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    html.H1('Welcome To Analytix Edge', className='display-3'),
                    width = {'size': 6, 'offset': 3}
                    ),
                ),
            dbc.Row(
                dbc.Col(
                    html.P(
                        """
                        At Analytix Edge, we are passionate about the transformative potential of data science. Our mission is to empower businesses, organizations, and individuals with the analytical tools and insights they need to thrive in today's data-driven world. We specialize in an array of data-driven services that go beyond traditional data science, including web scraping services and dashboard building.
                        """,
                        className = 'lead',
                        ),
                    ),
                ),
            dbc.Row(
                dbc.Col(
                    dbc.Button(
                        'Learn More',
                        color = 'primary',
                        href = './learn-more'
                        ),
                    width = {
                        'size': 2,
                        'offset': 5
                        }
                    ),
                ),
            ],
        fluid = True,
        )
