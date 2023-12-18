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
            html.H1('Welcome to the AnalytixEdge'),
            style = {
                'textAlign':'center'
            }
        ),
        html.Div(
            [
                dcc.Link(
                    " " + page['name']+" | ", href=page['path'],
                    style={'text-decoration':'none', 'font-size':'16px'},
                )
                for page in dash.page_registry.values()
            ],
            style = {
                'textAlign':'right'
            }
        ),
        html.Hr(),
        dash.page_container
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
