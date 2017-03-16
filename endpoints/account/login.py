from account import Account
from flask import jsonify, request
from flask.ext.restful import Resource, reqparse

from library.authentication import Authentication


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
        user_name = data.get('user_name')
        password = data.get('password')
        if Authentication.check_login(user_name, password):
            user_info = Account.get_user(user_name)
            user_info.pop('_id')
            return user_info
        else:
            data = {"response": "Bad Login"}
            return jsonify(data), 500
