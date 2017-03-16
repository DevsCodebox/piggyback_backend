from flask import jsonify, request, make_response
from flask.ext.restful import Resource, reqparse

from library.connections import Connections


class UpdateFriends(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(UpdateFriends, self).__init__()


    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)

        friend_list = data.get('friend_list')
        ssid = data.get('ssid')
        response = {}
        response['response'] = Connections.update_friends(ssid, friend_list)
        if response['status'] != True:
            return make_response(jsonify(response), 500)
        else:
            return jsonify(response)