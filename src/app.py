import dash  # pip install dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components

# Code from: https://github.com/plotly/dash-labs/tree/main/docs/demos/multi_page_example1

app = dash.Dash(
    __name__, external_stylesheets=[dbc.themes.SLATE], use_pages=True
)

navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="About",
    ),
    brand="",
    color="secondary",
    dark=True,
    className="mb-1",
)
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "15%",
    "padding": "2rem 1rem",
    'height': '100%'
    #"background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
sidebar = html.Div(
    [
        html.Div(
            [
                html.Img(src = './assets/images/android-chrome-192x192.png', style = {'margin-top': '10%', 'margin-left': '10%'}),
                ]
            ),
        #html.H1("Analytix Edge", className="display-2", style = {'margin-top': '20px', 'offset': 20, 'text-align': 'center'}),
        html.Hr(),
        html.P(
            "Sharper Insights", className = 'lead display-8', style = {'text-align': 'center'}
            ),
        html.P(
            "With", className = 'lead display-8', style = {'text-align': 'center'}
            ),
        html.P(
            "Deeper Impact", className="lead display-8", style = {'text-align': 'center'}
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(page['name'], href=page['path'])
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className = 'sidebar',
    style=SIDEBAR_STYLE,
)

app.layout = dbc.Container(html.Div([
    navbar, sidebar, dash.page_container
]), fluid=True)

if __name__ == "__main__":
    app.run_server(debug=True)
