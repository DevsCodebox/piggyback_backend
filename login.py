from flask import Flask, jsonify, url_for, redirect, request
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from authentication import Authentication
from account import Account

class Login(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(Login, self).__init__()


    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad Login"}
            return jsonify(data)
        user_id = data.get('user_name')
        password = data.get('password')
        if Authentication.check_login(user_id, password):
            user_info = Account.get_user(user_id)
            return {"response": "test"}
        else:
            data = {"response": "Bad Login"}
            return jsonify(data)