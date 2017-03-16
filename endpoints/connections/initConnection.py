from flask import jsonify, request, make_response
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
        user_name = data.get('user_name')
        ssid = data.get('ssid')
        ssid_strength = data.get('ssid_strength')
        response = {}
        if Connections.init_connections(user_name, ssid, ssid_strength):
            response['response'] = "SSID initialised"
            return jsonify(response)
        else:
            response['response'] = "SSID created and initialized"
            return jsonify(response)