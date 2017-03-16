from flask import jsonify, request, make_response
from flask.ext.restful import Resource, reqparse

from library.connections import Connections


class GetCriteriaUsed(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(GetCriteriaUsed, self).__init__()

    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)

        ssid = data.get('ssid')
        result = Connections.get_criteria_used(ssid)
        if result:
            return result
        else:
            return make_response(jsonify(result), 500)
