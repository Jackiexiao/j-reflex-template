from typing import Callable

import reflex as rx

from jweb.navigation import jweb_sidebar
from jweb.styles import BACKGROUND_COLOR


def template(page: Callable[[], rx.Component]) -> rx.Component:
    return rx.box(
        jweb_sidebar,
        page(),
        rx.logo(),
        background_color=BACKGROUND_COLOR,
        padding_bottom="4em",
    )
