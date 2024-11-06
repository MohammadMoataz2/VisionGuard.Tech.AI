import reflex as rx
import reflex_webcam as webcam
import base64
from .api_connector import send_to_analyze

# Webcam reference in the DOM
WEBCAM_REF = "webcam"


class State(rx.State):
    state: bool = False
    color: str = "red"
    status_text: str = "Face Not Detected"
    loading: bool = False
    progress_value: int = 0
    send: bool = True
    options_after: bool = False
    images: list = []
    analyze_face_state: bool = True
    face_analyze_result: dict = dict()
    analyze_options: bool = False

    # Attributes for face analysis results
    age: str = ""
    gender: str = ""
    emotion: str = ""
    race: str = ""

    def handle_screenshot(self, img_data_uri: str):
        """Handle the webcam screenshot as a base64 URI and process it."""
        if img_data_uri and (self.progress_value < 100):
            base64_image = img_data_uri.split(",")[1]  # Remove "data:image/jpeg;base64,"
            image_bytes = base64.b64decode(base64_image)
            self.images.append(image_bytes)

            # Simulate face detection
            result = send_to_analyze(image_bytes, 5020)
            if result["predictions"][0]["face"]:
                self.state = True
                self.color = "green"
                self.status_text = "Face Detected"
                self.progress_value += 1
            else:
                self.state = False
                self.color = "red"
                self.status_text = "Face Not Detected"

        # Once the progress reaches 100%, analyze face attributes
        if self.progress_value >= 100 and self.analyze_face_state:
            self.face_analyze_result = send_to_analyze(self.images[0], 5021)
            self.age = str(self.face_analyze_result["predictions"][0]["age"])
            gender_predictions = self.face_analyze_result["predictions"][0]["gender"]
            self.gender = max(gender_predictions, key=gender_predictions.get)  # Most likely gender
            self.race = self.face_analyze_result["predictions"][0]["race"]
            self.emotion = self.face_analyze_result["predictions"][0]["emotion"]

            # Update states to display analysis results
            self.analyze_face_state = False
            self.send = False
            self.state = True
            self.options_after = True
            self.analyze_options = True

    def restart_page(self):
        """Reset the state for a new analysis."""
        self.analyze_face_state = True
        self.state = False
        self.color = "red"
        self.status_text = "Face Not Detected"
        self.loading = False
        self.progress_value = 0
        self.send = True
        self.options_after = False
        self.analyze_options = False


def webcam_display_component(ref: str) -> rx.Component:
    """Component to display the webcam feed."""
    return rx.box(
        webcam.webcam(id=ref),
    )


def webcam_page() -> rx.Component:
    """Main page component with webcam and status display."""
    return rx.container(
        rx.vstack(
            rx.heading("🛡️ Vision Guard", font_size="70px"),
            justify="start",
            align_items="center",
            padding_top="50px",
            min_height="10vh",
        ),
        rx.center(
            webcam_display_component(WEBCAM_REF),
            padding_top="3em",
        ),
        rx.center(
            rx.box(
                rx.text(State.status_text, color="white", font_size="20px"),
                background=State.color,
                width="100%",
                height="50px",
                align_items="center",
                justify_content="center",
                display="flex",
                margin_top="10px",
            )
        ),
        rx.center(
            rx.progress(value=State.progress_value, max=100, width="50%", height="20px", color="blue"),
            padding_top="10px",
        ),
        # Invisible button that triggers screenshot capture
        rx.button(
            "",
            on_click=webcam.upload_screenshot(
                ref=WEBCAM_REF,
                handler=State.handle_screenshot,
            ),
            id="update-trigger",
            style={"display": "none"}
        ),
        rx.cond(
            State.send,
            rx.script(
                """
                setInterval(function() {
                    document.getElementById("update-trigger").click();
                }, 100);
                """
            )
        ),
        # Display analyzed attributes with labels above each input
        rx.cond(
            State.analyze_options,
            rx.hstack(
                rx.vstack(
                    rx.text("Age", font_weight="bold"),
                    rx.input(default_value=State.age, placeholder="Age", read_only=True),
                    align_items="center",
                ),
                rx.vstack(
                    rx.text("Gender", font_weight="bold"),
                    rx.input(default_value=State.gender, placeholder="Gender", read_only=True),
                    align_items="center",
                ),
                rx.vstack(
                    rx.text("Emotion", font_weight="bold"),
                    rx.input(default_value=State.emotion, placeholder="Emotion", read_only=True),
                    align_items="center",
                ),
                rx.vstack(
                    rx.text("Race", font_weight="bold"),
                    rx.input(default_value=State.race, placeholder="Race", read_only=True),
                    align_items="center",
                ),
                spacing="25px",  # Space between each input group
                justify="center",
                align_items="center",
                margin_top="20px",
            ),
        ),
        # Buttons for actions after analysis
        rx.cond(
            State.options_after,
            rx.hstack(
                rx.button(
                    "Continue",
                    on_click=rx.redirect("/webcam-page"),
                    font_size="20px",
                    padding="10px 20px",
                ),
                rx.button(
                    "Retry",
                    on_click=State.restart_page,
                    font_size="20px",
                    padding="10px 20px",
                ),
                margin_top="20px",
                spacing="25px",
                justify="center",
                align_items="center",
            ),
        )
    )

app = rx.App()
app.add_page(webcam_page)
