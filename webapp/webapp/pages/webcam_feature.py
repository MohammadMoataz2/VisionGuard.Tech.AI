import reflex as rx
import reflex_webcam as webcam
import random
import time
from urllib.request import urlopen
from PIL import Image
from .api_connector import send_to_analyze
# Webcam reference in the DOM
WEBCAM_REF = "webcam"
import base64
class State(rx.State):
    last_screenshot: Image.Image | None = None
    last_screenshot_timestamp: str = ""
    state: bool = False
    color: str = "red"
    status_text: str = "Face Not Detected"
    loading: bool = False
    progress_value: int = 0  # Add an initial progress value for display

    def handle_screenshot(self, img_data_uri: str):
        """Handle the webcam screenshot as a base64 URI and process it."""



        if img_data_uri and (self.progress_value < 100):
            base64_image = img_data_uri

            # Remove the "data:image/jpeg;base64," part if it's included
            base64_image = base64_image.split(",")[1]

            # Decode the base64 string into bytes
            image_bytes = base64.b64decode(base64_image)

            # Simulate face detection for this example

            result = send_to_analyze(image_bytes, 5020)
            if result["predictions"][0]["face"]:
                self.state = True
                self.color = "green"
                self.status_text = "Face Detected"
                self.progress_value +=1  # Update progress on success
            else:
                self.state = False
                self.color = "red"
                self.status_text = "Face Not Detected"
                  # Reset progress on failure

def webcam_display_component(ref: str) -> rx.Component:
    """Component to display the webcam feed."""
    return rx.box(
        webcam.webcam(id=ref),
    )

def webcam_page() -> rx.Component:
    """Main page component with webcam and status."""
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
                ref=WEBCAM_REF,  # Using the correct reference
                handler=State.handle_screenshot,  # type: ignore
            ),
            id="update-trigger",
            style={"display": "none"}
        ),
        # JavaScript timer that triggers the hidden button every 100ms
        rx.script(
            """
            setInterval(function() {
                document.getElementById("update-trigger").click();
            }, 100);
            """
        )
    )

app = rx.App()
app.add_page(webcam_page)
