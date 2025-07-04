from flask import Flask, jsonify,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route("/users")
def get_users():
    return jsonify([
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
