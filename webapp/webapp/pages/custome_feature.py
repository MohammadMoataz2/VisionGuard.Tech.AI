import reflex as rx
from .webcam_feature import State

def custom_feature_page() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("🛡️ Vision Guard", font_size="70px", font_weight="bold"),
            # Center the heading
            rx.hstack(
                rx.vstack(
                    rx.text("Age", font_weight="bold", font_size="20px"),  # Increase font size
                    rx.heading(State.age, font_size="24px"),  # Increase heading font size
                    rx.slider(
                        default_value=40,
                        on_value_commit=State.change_age,
                        size="lg",
                    ),
                    width="200px",  # Increase width for more space
                    align_items="center",
                ),
                rx.vstack(
                    rx.text("Gender", font_weight="bold", font_size="20px"),  # Increase font size
                    rx.select(
                        ["Man", "Woman", "Prefer not to say"],
                        value=State.gender,
                        on_change=State.change_gender,
                        size="lg",
                        width="150px"
                    ),
                    align_items="center",
                ),
                rx.vstack(
                    rx.text("Emotion", font_weight="bold", font_size="20px"),  # Increase font size
                    rx.select(
                        ["angry", "fear", "neutral", "sad", "disgust", "happy", "surprise", "Prefer not to say"],
                        value=State.emotion,
                        on_change=State.change_emotion,
                        size="lg",
                        width="150px"
                    ),
                    align_items="center",
                ),
                rx.vstack(
                    rx.text("Race", font_weight="bold", font_size="20px"),  # Increase font size
                    rx.select(
                        ["asian", "white", "middle eastern", "indian", "latino", "black", "Prefer not to say"],
                        value=State.race,
                        on_change=State.change_race,
                        size="lg",
                        width="150px"
                    ),
                    align_items="center",
                ),
                spacing="5",  # Space between each input group
                justify="center",
                align_items="center",
                margin_top="30px",
                margin_bottom="50px"  # Increase margin bottom
            ),
            # Continue button centered below the form
            rx.button(
                "Continue",

                size="lg",
                width="200px",
                margin_top="30px",
                font_size="20px",
                on_click=rx.redirect("/search-engine-page"),
                color_scheme="teal",  # You can adjust the color scheme
                align_self="center",
            ),
            justify="center",
            align_items="center",
            padding_top="30px",  # 30px margin from top
            min_height="100vh",  # Full screen height
        ),
        justify="center",
        align_items="center"
    )
