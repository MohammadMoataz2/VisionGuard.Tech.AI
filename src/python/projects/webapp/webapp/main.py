import streamlit as st
import cv2
import numpy as np
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import requests
import json
import io
# Function to display the home page
def home_page():
    # Inject CSS to hide Streamlit warnings
    st.markdown(
        """
        <style>
        .stException {
            display: none;  /* Hide all warning messages */
        }
        .title {
            font-size: 70px;
            font-weight: 800;
            color: #C0C0C0;  /* Silver */
            font-family: 'Arial', sans-serif;
            text-shadow: 3px 3px rgba(0, 0, 0, 0.25);
            margin-top: 60px;
            margin-bottom: 40px;
            text-align: center;
        }
        .welcome-text {
            font-size: 24px;
            font-weight: 400;
            color: #FFFFFF;
            margin-bottom: 20px;
            text-align: center; /* Center align text */
        }
        .big-button {
            width: 200px;
            height: 70px;
            font-size: 20px;
            background-color: #363636;
            color: #FFFFFF;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            display: inline-block; /* Inline block for centering */
            text-align: center; /* Center text */
        }
        .big-button:hover {
            background-color: #444444; /* Button hover color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create columns for centering content and button
    col1, col2, col3 = st.columns([1, 10, 1])  # Adjust column ratios as needed

    with col2:  # Center column for content and button
        st.markdown("<h1 class='title'>🛡️ Vision Guard</h1>", unsafe_allow_html=True)

        # Check and initialize session state
        if 'welcome_displayed' not in st.session_state:
            st.session_state.welcome_displayed = False

        # Display welcome message and button
        if st.session_state.welcome_displayed:
            st.markdown("<h2 class='welcome-text'>Welcome to Vision Guard!</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2 class='welcome-text'>Please click the button to proceed.</h2>", unsafe_allow_html=True)
            st.markdown(
                "<p class='welcome-text'>This is an AI application designed to leverage your webcam and advanced algorithms to analyze and collect features.</p>",
                unsafe_allow_html=True
            )
            st.markdown(
                "<p class='welcome-text'>We will use your webcam to capture various features for analysis.</p>",
                unsafe_allow_html=True
            )

        # Create a centered button that triggers session state change
        if st.button('Continue', key='continue_button', use_container_width=True):
            # Update the session state to show the webcam page
            st.session_state.welcome_displayed = True
            st.session_state.page = "webcam"

# Function to display the webcam page and capture frames
def webcam_page():


    # FastAPI server details
    API_URL = "http://localhost:8011/api/v1/face_analysis/analyze-face/"
    AUTH = ("Foo", "Bar")  # HTTP Basic authentication credentials

    # Callback info to be sent with the image
    CALLBACK_INFO = {
        "callback_url": "http://localhost:5500/callback",
        "other_info": "Some info",
        "immediately": True
    }

    # Function to convert a frame (numpy array) to bytes
    def frame_to_bytes(frame):
        _, buffer = cv2.imencode('.png', frame)  # Encode frame as PNG
        return io.BytesIO(buffer).getvalue()  # Convert to bytes

    # Function to send an image file to the FastAPI server
    def send_image(image_bytes):
        files = {
            'callback_info': (None, json.dumps(CALLBACK_INFO), 'application/json'),  # Send JSON correctly
            'file': ('frame.png', image_bytes, 'image/png')  # Send the image bytes
        }

        response = requests.post(API_URL, files=files, auth=AUTH)

        if response.status_code == 200:
            print("Image sent successfully!")
            print("Response:", response.json())
            return response.json().get("face_detected", False)  # Access the 'face_detected' key
        else:
            print(f"Failed to send image. Status code: {response.status_code}")
            print("Error:", response.text)
            return False

    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Function to detect faces in an image
    def detect_faces(image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)  # Detect faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw green rectangle around faces
        return image, len(faces) > 0  # Return the image and face detection status

    # Set up Streamlit app
    st.title("Real-time Face Detection with Webcam")

    # Set up video capture
    video_capture = cv2.VideoCapture(0)  # 0 is the default camera
    stframe = st.empty()  # Placeholder for the video frame
    detection_text = st.empty()  # Placeholder for detection status

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Detect faces in the frame
        frame_with_faces, _ = detect_faces(frame)

        # Convert frame to bytes and send it to the server
        frame_bytes = frame_to_bytes(frame)
        face_detected = send_image(frame_bytes)

        # Convert the frame to RGB for display in Streamlit
        frame_rgb = cv2.cvtColor(frame_with_faces, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels="RGB", use_column_width=True)

        # Update detection status in Streamlit
        if face_detected:
            detection_text.success("Face Detected")
        else:
            detection_text.warning("No Face Detected")

    # Release the camera
    video_capture.release()


# Main app logic
if 'page' not in st.session_state:
    st.session_state.page = "home"  # Start on the home page

# Show the appropriate page based on the session state
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "webcam":
    webcam_page()
