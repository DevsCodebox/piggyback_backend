from flask import jsonify, request
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
        Transaction.add_transaction(data)
        data = {"response": "Successful request"}
        return jsonify(data)