"""The main Jweb App."""

from rxconfig import config

import reflex as rx

from jweb.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from jweb.pages.tools import tools
from jweb.pages.team import team
from jweb.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
