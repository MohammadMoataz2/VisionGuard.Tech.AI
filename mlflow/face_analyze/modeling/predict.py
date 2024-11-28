import mlflow.pyfunc
import pandas as pd
import base64


def predict(model_uri, image_bytes):
    # Load the model from MLflow
    model = mlflow.pyfunc.load_model(model_uri)

    # Prepare input data
    input_data = pd.DataFrame({"image_bytes": [image_bytes]})

    # Make predictions
    result = model.predict(input_data)
    return result


if __name__ == "__main__":
    # Read the image and encode it to base64
    with open("dataset/1.png", "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

    # Call the prediction function with the MLflow model URI
    model_uri = "models:/deepface_analysis_model/1"  # Adjust version as needed
    predictions = predict(model_uri, encoded_image)

    print(predictions)
