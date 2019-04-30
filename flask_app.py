# flask_app.py
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "Hello World! lalalala"

@app.route("/api")
def create_json():
	dic={'winter':'invierno','summer':'verano'}
	return jsonify(dic)

#@app.route("/api")
#def create_json():
#	return pd.DataFrame({'english':['winter','summer'],'spanish':['invierno','verano']}).to_json(orient='records')

@app.route("/api", methods=["POST","GET"])
#def post():
#	print(request.form)
#	return jsonify(request.form)

def get_post():
	if request.method == 'POST':
		dic=request.form.to_dict()
		dic['three']='tres'
		return jsonify(dic)
	else:
        	dic={'winter':'invierno','summer':'verano'}
        	return jsonify(dic)
