from flask import Flask, jsonify, url_for, redirect, request
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from authentication import Authentication
from transaction import Transaction


class AddTransaction(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()


    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad request"}
            return jsonify(data)
        Transaction.add_transaction(data)