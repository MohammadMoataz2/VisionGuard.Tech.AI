import reflex as rx
from rxconfig import config
from PIL import Image
from .pages.webcam_feature import webcam_page
from .pages.custome_feature import custom_feature_page

def welcome_page() -> rx.Component:
    return rx.container(
        # Top heading
        rx.vstack(
            rx.heading("🛡️ Vision Guard", font_size="70px", text_align="center"),
            justify="start",
            align_items="center",
            padding_top="50px",
            min_height="10vh",
        ),
        # Centered content
        rx.vstack(
            rx.text("Welcome to Vision Guard!", font_size="30px", text_align="center"),
            rx.text(
                "This is an AI application designed to leverage your webcam "
                "and advanced algorithms to analyze and collect features.",
                font_size="20px",
                text_align="center",
            ),
            # Buttons aligned side by side
            rx.hstack(
                rx.button(
                    "Go to Webcam Page",
                    on_click=rx.redirect("/webcam-page"),
                    font_size="20px",
                    padding="10px 20px",
                    width="200px",  # Fixed width for uniform buttons
                    background_color="blue",
                    color="white",
                    border_radius="5px",
                ),
                rx.button(
                    "Go to Custom Feature Page",
                    on_click=rx.redirect("/custom-feature-page"),
                    font_size="20px",
                    padding="10px 20px",
                    width="200px",  # Fixed width for uniform buttons
                    background_color="green",
                    color="white",
                    border_radius="5px",
                ),
                spacing="5",  # Space between buttons
                justify="center",
            ),
            align_items="center",
            spacing="5",
            justify="center",
            min_height="75vh",
        ),
    )

# Initialize and configure the app
app = rx.App()

# Add pages with their routes
app.add_page(welcome_page, route="/")
app.add_page(webcam_page, route="/webcam-page")
app.add_page(custom_feature_page, route="/custom-feature-page")

# Run the app
if __name__ == "__main__":
    app.run()
