from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/about')
def about():
    return "This is the about page."


@app.route('/callback', methods=['POST'])
def receive_callback():
    # Get the JSON data from the request
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    task_id = data.get('task_id')
    result = data.get('result')

    # Process the data as needed (e.g., log it, save to a database, etc.)
    print(f"Received callback for task_id: {task_id}, result: {result}")

    # Send a response back
    return jsonify({"status": "success", "task_id": task_id}), 200


if __name__ == '__main__':
    app.run(port=5000)
