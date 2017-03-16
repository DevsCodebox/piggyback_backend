from flask import jsonify, request
from flask.ext.restful import Resource, reqparse

from library.transaction import Transaction


class ClientPollingUpdate(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(ClientPollingUpdate, self).__init__()

    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad request"}
            return jsonify(data)

        ssid = data.get('ssid')
        user_name = data.get('user_name')
        credit = data.get('credits')
        bandwidth = data.get('bandwidth')
        remaining = Transaction.client_polling_update(ssid, user_name, credit, bandwidth)
        data = {"credits_remaining": remaining}
        return jsonify(data)