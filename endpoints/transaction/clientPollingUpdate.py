from flask import jsonify, request, make_response
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
        credit_usage = data.get('credit_usage')
        bandwidth = data.get('bandwidth')
        remaining = Transaction.client_polling_update(ssid, user_name, credit_usage, bandwidth)
        data = {"credits_remaining": remaining}
        if remaining:
            return jsonify(data)
        else:
            return make_response(jsonify({"response":"fail"}), 500)
