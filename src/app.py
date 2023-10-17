from components import navbar
from pages import home
from dash import html, dcc
import dash
import dash_bootstrap_components as dbc

#https://community.plotly.com/t/structuring-a-large-dash-application-best-practices-to-follow/62739

app = dash.Dash(
        __name__,
        use_pages = True,
        external_stylesheets=[
            dbc.themes.SLATE,
            dbc.icons.FONT_AWESOME
            ],
        meta_tags = [
            {
                'name': 'viewport',
                'content': 'width=device-width, initial-scale=1'
                }
            ],
        title = 'AnalytixEdge'
        )


def page_layout():
    return html.Div(
            [
                navbar,
                html.Div(
                    [
                        dbc.Container(
                            dcc.Link(
                                page['name'] +" | ", href = page['path']
                                ),
                            className = 'my-2'
                            ),
                        ]
                    for page in dash.page_registry.values()
                    ),
                dash.page_container
                ]
            )

app.layout = dbc.Container(
        html.Div(
            [
                dash.page_container
                ]
            ),
        fluid = True
        )


if __name__ == '__main__':
    app.run_server(
            debug = True
            )
