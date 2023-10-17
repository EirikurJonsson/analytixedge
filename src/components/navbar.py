import dash_bootstrap_components as dbc
from dash import Input, Output, State, html, callback
from dash_bootstrap_components._components.Container import Container


ANALYTIXEDGELOG = '../assets/images/favicon-32x32.png'
search_bar = dbc.Row(
        children = [
            dbc.Col(
                dbc.Input(
                    type = 'search',
                    placeholder = 'Search'
                    )
                ),
            dbc.Col(
                dbc.Button(
                    "Seach", 
                    color = 'primary',
                    className = 'ms-2',
                    n_clicks = 0
                    ),
                width = 'auto'
                ),
            ],
        className = 'g0 ms-auto flex-nowrap mt-3 mt-md-0',
        align = 'center',
        )

navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    src = ANALYTIXEDGELOG, height = '30px'
                                    )
                                ),
                            dbc.Col(
                                dbc.NavbarBrand(
                                    "Analytix Edge: Sharper Insights, Deeper Impact",
                                    className = 'ms-2'
                                    )
                                )
                            ],
                        align = 'center',
                        className = 'g-0',
                        ),
                    href = '#',
                    style = {
                        "textDecoration": 'none',
                        }
                    ),
                dbc.NavbarToggler(
                    id = 'navbar-toggler',
                    n_clicks = 0
                    ),
                dbc.Collapse(
                    search_bar,
                    id = 'navbar-collapse',
                    is_open = False,
                    navbar = True,
                    )
                ]
            ),
        color = 'dark',
        dark = True
    )

@callback(
        Output('navbar-collapse', 'is_open'),
        Input('navbar-toggler', 'n_clicks'),
        State('navbar-collapse', 'is_open')
        )
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open

    return is_open
