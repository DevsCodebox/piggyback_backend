from flask import jsonify, request, make_response
from flask.ext.restful import Resource, reqparse

from library.connections import Connections


class UpdateSSIDStrength(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(UpdateSSIDStrength, self).__init__()


    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)
        ssid = data.get('ssid')
        ssid_strength = data.get('ssid_strength')
        response = {}
        if Connections.update_ssid_strength(ssid, ssid_strength):
            response['response'] = "SSID updated"
            return jsonify(response)
        else:
            response['response'] = "SSID failed to update"
            return make_response(jsonify(response), 500)