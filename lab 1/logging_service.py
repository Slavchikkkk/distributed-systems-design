from flask import Flask, request, abort

app = Flask(__name__)

messages = {}

@app.route("/logging_service", methods=["POST", "GET"])
def log_request():
    if request.method == "POST":
        id = request.form['id']
        message = request.form['msg']
        messages[id] = message
        print("Received message:", message)
        return "Success"
    elif request.method == "GET":
        return messages
    else:
        abort(400)

if __name__ == '__main__':
    app.run(port=5001)
