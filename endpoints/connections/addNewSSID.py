from flask import jsonify, request
from flask.ext.restful import Resource, reqparse

from library.connections import Connections


class AddNewSSID(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(AddNewSSID, self).__init__()


    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)

        user_name = data.get('user_name')
        ssid = data.get('ssid')
        ssid_strength = data.get('ssid_strength')

        friends = data.get('friends')

        response = {}
        if Connections.add_new_ssid(user_name, ssid, ssid_strength, friends):
            response['response'] = "SSID created"
        else:
            response['response'] = "SSID Failed to Create"
        return jsonify(response)