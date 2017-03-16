from flask import jsonify, request, make_response
from flask.ext.restful import Resource, reqparse

from library.transaction import Transaction
from library.connections import Connections

class AddTransaction(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(AddTransaction, self).__init__()


    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad request"}
            return jsonify(data)

        ssid = data.get('ssid')
        host = Connections.get_user_name(ssid)
        data['host'] = host
        status = Transaction.add_transaction(data)
        if status:
            data = {"response": "Successful request"}
            return jsonify(data)
        else:
            return make_response(jsonify({"response":"failed"}), 500)