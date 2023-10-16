from components import navbar
import dash
from dash import html
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
                dbc.Container(
                    dash.page_container,
                    className = 'my-2'
                    )
                ]
            )

app.layout = page_layout


if __name__ == '__main__':
    app.run_server(
            debug = True
            )
