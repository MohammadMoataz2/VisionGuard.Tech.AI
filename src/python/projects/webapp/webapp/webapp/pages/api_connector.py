import base64
import json
import requests

def send_to_analyze(encoded_image, endpoint_port):
    # Convert image bytes to base64
    base64_encoded_image = base64.b64encode(encoded_image).decode('utf-8')

    # Create the payload in dataframe_split formatport
    payload = {
        "dataframe_split": {
            "columns": ["image_bytes"],
            "data": [[base64_encoded_image]]  # Use the base64 string instead of raw bytes
        }
    }

    # Send request to the MLflow model server
    response = requests.post(f"http://localhost:{endpoint_port}/invocations", json=payload)

    # Parse the response as JSON
    response_json = response.json()


    return response_json