from flask import Flask, request
from flask_restful import Resource, Api
from flask.ext.jsonpify import jsonify
import os

app = Flask(__name__)
api = Api(app)


class LightOff(Resource):
    def get(self):
        os.system('python LightOff.py')
        return jsonify("success")


class LightOn(Resource):
    def get(self):
        os.system('python LightOn.py')
        return jsonify("success")


api.add_resource(LightOff, '/api/lightoff')
api.add_resource(LightOn, '/api/lighton')

if __name__ == '__main__':
    app.run(port='5000')
