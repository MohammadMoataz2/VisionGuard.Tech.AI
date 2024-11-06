import reflex as rx




def custom_feature_page() -> rx.Component:
    return rx.container(

        rx.vstack(
            rx.heading("🛡️ Vision Guard", font_size="70px"),
            justify="start",
            align_items="center",
            padding_top="50px",
            min_height="10vh",
        ),

    )
