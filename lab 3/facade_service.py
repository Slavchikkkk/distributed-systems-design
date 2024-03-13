from flask import Flask, request, abort, jsonify
import requests
import uuid
from pyotp import random

app = Flask(__name__)

MESSAGES_SERVICE_URL = "http://localhost:5004/messages"


@app.route("/facade_service", methods=["POST", "GET"])
def handle_request():
    if request.method == "POST":
        message = request.form.get("msg")
        if not message:
            return jsonify({"error": "Message not provided"}), 400

        id = str(uuid.uuid4())
        data = {"id": id, "msg": message}
        port = random.randint(5001, 5003)
        logging_service = "http://localhost:{}/logging_service".format(port)
        response = requests.post(logging_service, data=data)
        response.raise_for_status()

        return jsonify({"id": id, "msg": message}), 200

    elif request.method == "GET":
        try:
            port = random.randint(5001, 5003)
            logging_service = "http://localhost:{}/logging_service".format(port)
            log_response = requests.get(logging_service, timeout=5)
            log_response.raise_for_status()
            message_response = requests.get(MESSAGES_SERVICE_URL, timeout=5)
            message_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return jsonify({"error": f"Error fetching data: {str(e)}"}), 500
        return jsonify({"logs": log_response.text, "messages": message_response.text}), 200
    else:
        return abort(400)


if __name__ == "__main__":
    app.run(port=5000)
