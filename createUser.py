from flask import Flask, jsonify, url_for, redirect, request
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from account import Account
import json


class CreateUser(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()

# def create_account(self, first_name, last_name, user_name, email, date_of_birth, password, password_confirm):
    def post(self):
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        user_name = data.get('user_name')
        email = data.get('email')
        date_of_birth = data.get('date_of_birth')
        password = data.get('password')
        password_confirm = data.get('password_confirm')
        if Account.create_account(first_name, last_name, user_name, email, date_of_birth, password, password_confirm):
            response = {"response": "Account Created"}
        else:
            response = {"response": "Account Creation Failed"}
        return jsonify(response)
