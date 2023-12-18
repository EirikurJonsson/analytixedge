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
            className='row',
            children=[
                html.Div(
                    className='one columns',
                    children=[
                        html.H1('Welcome to the AnalytixEdge', style = {'textAlign':'center'}),
                    ]
                )
            ]
        ),
        html.Div(
            children = [
                dcc.Link(
                    page['name']+"  ", href=page['path']
                    , style = {'textAlign':'center', 'margin-right': '20px', 'font-size':'22px'})
                for page in dash.page_registry.values()
            ],
                style={'text-align': 'right'}
        ),
        html.Hr(),
        dash.page_container
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
