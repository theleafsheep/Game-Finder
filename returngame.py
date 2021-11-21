from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {}

@app.route("/")
def return_game():
    answers = request.args.get('answers')
    print(answers)
    return "Omori"


@app.route("/list")
def list():
    return users