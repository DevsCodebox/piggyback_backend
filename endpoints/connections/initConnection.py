from flask import jsonify, request
from flask.ext.restful import Resource, reqparse

from library.connections import Connections


class InitConnection(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(InitConnection, self).__init__()


    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)
        ssid = data.get('ssid')
        response = {}
        if Connections.init_connections(ssid):
            response['response'] = "SSID initialised"
        else:
            response['response'] = "SSID failed to update"
        return jsonify(response)