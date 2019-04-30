# flask_app.py
from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "Hello World! lalalala"

@app.route("/api")
def jsonify():
	dic={'winter':'invierno','summer':'verano'}
	return jsonify(dic)
