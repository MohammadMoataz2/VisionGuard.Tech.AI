import requests
import cv2
import base64

# Prepare the input image
image_path = "dataset/1.png"
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    raise ValueError(f"Error: Could not read the image at {image_path}")

# Encode the image to bytes and then to base64
_, buffer = cv2.imencode('.jpg', image)
image_bytes = buffer.tobytes()
image_base64 = base64.b64encode(image_bytes).decode('utf-8')  # Encode to base64

# Prepare the request payload
data = {
    "instances": [{"image_bytes": image_base64}]  # Use base64 encoded string
}

# Send the request
response = requests.post("http://localhost:5002/invocations", json=data)

# Print the response
print(response.json())
