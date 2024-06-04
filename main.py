import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Diccionario para almacenar usuarios
users = {}

@app.route("/")
def root():
    return "root"

@app.route("/users/<user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if user:
        query = request.args.get("query")
        if query:
            user["query"] = query
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = data.get("id")
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400
    users[user_id] = data
    return jsonify({"status": "user created", "user": data}), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

