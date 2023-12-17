import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Set up the app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SLATE],
    use_pages=True)

app.layout = html.Div(
    [
        html.Div(
            'Wellcome to the AnalytixEdge'
        ),
        html.Div(
            [
                dcc.Link(
                    page['name']+" | ", href=page['path']
                )
                for page in dash.page_registry.values()
            ]
        ),
        html.Hr(),
        dash.page_container
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
