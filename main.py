from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/pathetic')
def pathetic():
    return jsonify("Pathetic": "Welcome to pathetic"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
