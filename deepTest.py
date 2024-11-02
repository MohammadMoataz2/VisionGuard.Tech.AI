import requests
import base64
import json

# Read the image and encode it to base64
with open("dataset/1.png", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

# Create the payload in dataframe_split format
payload = {
    "dataframe_split": {
        "columns": ["image_bytes"],
        "data": [[encoded_image]]
    }
}

# Send request to the MLflow model server
response = requests.post("http://localhost:5003/invocations", json=payload)

# Print the result
print(json.dumps(response.json(), indent=2))
