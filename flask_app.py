# flask_app.py
from flask import Flask
from flask import jsonify
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "Hello World! lalalala"

#@app.route("/api")
#def create_json():
#	dic={'winter':'invierno','summer':'verano'}
#	return jsonify(dic)

@app.route("/api")
def create_json():
	return pd.DataFrame({'english':['winter','summer'],'spanish':['invierno','verano']}).to_json(orient='records')
