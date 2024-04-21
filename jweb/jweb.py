"""The main Jweb App."""

import reflex as rx

from jweb.pages.index import index
from jweb.pages.team import team
from jweb.pages.tools import tools
from jweb.pages.form import form
from jweb.styles import THEME

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    font_family="Microsoft YaHei",
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
app.add_page(form, route="/form")
