import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = dbc.Container(
    [
        html.Div(
            children = [
            html.H1("Our Services", className="display-4"),

            html.P("""
            What I do best is within Data Science - the whole thing from start to finish. This includes
            the data engineering from raw data to finished features and the model fine tuning. Depending on
            the use case I can also create fast flask apis that make that data available to other purposes
            or use them to build you a custom dashboard.
            """),
            ]
        ),
        html.Div(
            [
                html.Img(src = '../assets/images/ds_programmingbot.jpg', style = {'height':'650px'}) 
            ],
            style = {'textAlign':'center'}
        ),
        html.Div(
            [
                html.P(
                    """
                    What sets this service apart from others is the professional level of data science work best
                    practices and web scraping. Not a lot of businesses consider web scraping when considering 
                    data sources - but often - publicly available data can be gatherd from various places online.
                    Reason why some companies dont consider web scraping is due to idea of manually copying and pasting
                    the data to some sheet. Using modern webframeworks like scrapy and playwright we can automate 
                    this process and get cheap valuable data for almost no cost.
                    """
                ),
                html.Div(
                    [
                        html.Img(src = '../assets/images/webscrappingLogo_1.jpg', style = {'height':'650px'}) 
                    ],
                    style = {'textAlign':'center'}
                )
            ],
        )
    ],
    style={'padding': '20px'}
)


