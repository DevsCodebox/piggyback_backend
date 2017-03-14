from flask import Flask, jsonify, url_for, redirect, request
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from authentication import Authentication
from transaction import Transaction

import json


class GetReceipt(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()


    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)
        user_id = data.get('user_id')
        start_date = data.get('start')
        end_date = data.get('end')

        receipt = Transaction.get_receipt(user_id,start_date, end_date)
        if receipt:
            return jsonify(json.dumps(receipt),  mimetype='application/json')
        else:
            data = {"response": "No Receipt"}
            return jsonify(data)