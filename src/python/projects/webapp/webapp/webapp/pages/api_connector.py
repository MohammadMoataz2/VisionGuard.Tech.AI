import base64
import json
import requests
from requests.auth import HTTPBasicAuth

def send_to_analyze(encoded_image, tag, task_name):
    # Convert image bytes to base64
    base64_encoded_image = base64.b64encode(encoded_image).decode('utf-8')

    # Create the payload in dataframe_split format
    files = {
        'file': ('image.jpg', encoded_image, 'image/jpeg')  # Sending the image file as bytes
    }

    # Send request to the MLflow model server with Basic Authentication
    username = "Foo"
    password = "Bar"
    response = requests.post(
        f"http://localhost:{8000}/api/v1/{tag}/{task_name}",
        files=files,
        auth=HTTPBasicAuth(username, password)  # Include the HTTP Basic Authentication
    )

    # Parse the response as JSON
    response_json = response.json()

    return response_json
