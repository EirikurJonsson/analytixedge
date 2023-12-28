"""The dashboard page."""
from analytixedge.templates import template

import reflex as rx

import yfinance as yf


@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Dashboard", font_size="3em"),
        rx.text("Welcome The Testing Dashboard!"),
        rx.text(
            """
            Lets look at a simple example of plotting that can be done. This is easy and lets take some input and plot it.
            """,
            rx.code("{your_app}/pages/dashboard.py"),
        ),
    )
