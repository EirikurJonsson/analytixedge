"""The home page of the app."""

from analytixedge import styles
from analytixedge.templates import template
import os
print(os.getcwd())

import reflex as rx


@template(route="/about", title="About")
def about() -> rx.Component:
    """The about page.

    Returns:
        The UI for the about page.
    """
    with open("analytixedge/page_content/about.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)
