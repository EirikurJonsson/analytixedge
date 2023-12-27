"""The home page of the app."""

from analytixedge import styles
from analytixedge.templates import template

import reflex as rx


@template(route="/", title="Home", image="/favicon-32x32.png")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)
