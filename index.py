from flask import Flask, request
from flask_restful import Resource, Api
from flask.ext.jsonpify import jsonify
import os

app = Flask(__name__)
api = Api(app)

@app.route("/lightoff")
def lightOff(self):
    os.system('python LightOff.py')
    return jsonify("success")

@app.route("/lighton")
def lightOn(self):
    os.system('python LightOn.py')
    return jsonify("success")

if __name__ == '__main__':
    app.run(port='5000')
