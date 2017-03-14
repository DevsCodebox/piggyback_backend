from flask import Flask, jsonify, url_for, redirect, request
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from authentication import Authentication
from account import Account

class ChangePassword(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()


    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad Login"}
            return jsonify(data)
        user_id = data.get('user_id')
        password = data.get('password')
        prev_password = data.get('prev_password')
        password_confirm = data.get('password_confirm')
        if Account.change_password(user_id, prev_password, password, password_confirm):
            return {'response': 'ok'}
        else:
            return {'response': 'Bad Request'}
