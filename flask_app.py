# flask_app.py

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

#create a database

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

__tablename__ = "mydb"

import config

app = Flask(__name__)

# Set debug status
if config.ENVIRONMENT == 'development':
    app.config["DEBUG"] = True
else:
    app.config["DEBUG"] = False

# Set db config
for key, value in config.DB[config.ENVIRONMENT].items():
    app.config[key] = value
db = SQLAlchemy(app)


##
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

## connecting DB with API

