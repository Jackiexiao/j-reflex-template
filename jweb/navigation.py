import reflex as rx
from jweb.components.color_mode_button import color_mode_button


def sidebar_link(text: str, href: str, icon: str):
    return rx.link(
        rx.flex(
            rx.icon_button(
                rx.icon(tag=icon, weight=16, height=16),
                variant="soft",
            ),
            text,
            py="2",
            px="4",
            spacing="3",
            align="baseline",
            direction="row",
        ),
        href=href,
        width="100%",
        border_radius="8px",
        _hover={
            "background": "rgba(255, 255, 255, 0.1)",
            "backdrop_filter": "blur(10px)",
        },
    )


def sidebar(
    *sidebar_links,
    **props,
) -> rx.Component:
    logo_src = props.get("logo_src", "/logo.jpg")
    heading = props.get("heading", "NOT SET")
    return rx.vstack(
        rx.hstack(
            rx.image(src=logo_src, height="28px", border_radius="8px"),
            rx.heading(
                heading,
                size="7",
            ),
            width="100%",
            spacing="7",
        ),
        rx.divider(margin_y="3"),
        rx.vstack(
            *sidebar_links,
            padding_y="1em",
        ),
        width="250px",
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        align_items="left",
        z_index="10",
        backdrop_filter="blur(10px)",
        padding="2em",
    )


jweb_sidebar = sidebar(
    sidebar_link(text="Dashboard", href="/", icon="bar_chart_3"),
    sidebar_link(text="Tools", href="/tools", icon="settings"),
    sidebar_link(text="Team", href="/team", icon="users"),
    sidebar_link(text="Form", href="/form", icon="table_2"),
    logo_src="/logo.jpg",
    heading="JwebDemo",
)


class State(rx.State):
    pass


def navbar(heading: str) -> rx.Component:
    return rx.hstack(
        rx.heading(heading, size="7"),
        rx.spacer(),
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    "Menu",
                    rx.icon("chevron-down", weight=16, height=16),
                    variant="soft",
                ),
            ),
            rx.menu.content(
                rx.menu.item("Settings"),
                rx.menu.item("Profile"),
                rx.menu.item("Logout"),
                variant="soft",
            ),
            variant="soft",
        ),
        color_mode_button(),
        position="fixed",
        width="calc(100% - 250px)",
        align="center",
        top="0px",
        z_index="1000",
        padding_x="2em",
        padding_top="2em",
        padding_bottom="1em",
        backdrop_filter="blur(10px)",
    )
