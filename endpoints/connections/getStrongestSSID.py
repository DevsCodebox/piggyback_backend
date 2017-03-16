from flask import jsonify, request
from flask.ext.restful import Resource, reqparse

from library.connections import Connections


class GetStrongestSSID(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(GetStrongestSSID, self).__init__()


    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)

        ssid_list = data.get('ssid_list')
        response = {}
        response['SSID'] = Connections.strongest_ssid(ssid_list)
        return jsonify(response)