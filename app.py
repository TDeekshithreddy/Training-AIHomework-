from flask import Flask, request
from flask_restplus import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

# get API to return {"Receiver": "Cisco is the best!"}
@api.route('/api/v1/info')
class Cisco(Resource):
    def get(self):
        return {"Receiver": "Cisco is the best!"}


# POST API
"""
This route should send a GET request to that endpoint,
 and return the payload of that request as the response for the route.
"""
@api.route('/api/v1/ping')
class Foobar(Resource):
    def post(self):
        json_data = request.json
        payload = requests.get(json_data.get('url'))
        return payload


# Get API health
@api.route('/health')
class Health(Resource):
    def get(self):
        return {"Receiver": "Cisco is the best!"}


if __name__ == '__main__':
    app.run(port=8080, debug=True)
