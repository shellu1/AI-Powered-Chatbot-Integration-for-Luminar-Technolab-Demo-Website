from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('shel.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    response = requests.post(
        "http://localhost:5005/webhooks/rest/webhook",  # Rasa server URL
        json={"sender": "user", "message": user_message}
    )
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
