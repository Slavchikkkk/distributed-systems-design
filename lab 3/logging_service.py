from flask import Flask, request, abort
import hazelcast
import argparse

app = Flask(__name__)

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, required=True)
args = parser.parse_args()

hz = hazelcast.HazelcastClient(cluster_name="dev", cluster_members=[])
messages = hz.get_map("messages").blocking()


@app.route("/logging_service", methods=["POST", "GET"])
def log_request():
    if request.method == "POST":
        id = request.form['id']
        message = request.form['msg']
        messages.put(id, message)
        print("Received message:", message)
        return "Success"
    elif request.method == "GET":
        keys = messages.key_set()
        arr = []
        for key in keys:
            value = messages.get(key)
            arr.append(value)
        return "\n".join(arr)
    else:
        abort(400)

if __name__ == '__main__':
    app.run(port=args.port)
