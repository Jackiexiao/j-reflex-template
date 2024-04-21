import reflex as rx
from jweb.navigation import navbar
from jweb.template import template
from jweb.components.profile_form import profile_form


@template
def form() -> rx.Component:
    return rx.box(
        navbar(heading="Form"),
        rx.box(
            profile_form(),
            margin_top="calc(50px + 2em)",
        ),
        padding_left="250px",
    )
