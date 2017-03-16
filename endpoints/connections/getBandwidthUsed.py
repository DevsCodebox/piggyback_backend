from flask import jsonify, request, make_response
from flask.ext.restful import Resource, reqparse

from library.connections import Connections


class GetBandwidthUsed(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(GetBandwidthUsed, self).__init__()

    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)

        response = {}
        ssid = data.get('ssid')
        response['SSID'] = Connections.get_bandwidth_used(ssid)
        if response['SSID']:
            return jsonify(response)
        else:
            return make_response(jsonify(response), 500)
