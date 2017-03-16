from flask import jsonify, request, make_response
from flask.ext.restful import Resource, reqparse

from library.account import Account


class CreateUser(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(CreateUser, self).__init__()


    def post(self):
        """
        data reqs:
        {"first_name":"test",
        "last_name":"test",
        "email":"email",
        "date_of_birth":"temp",
        "password":"temp",
        "password_confirm":"temp"
        }

        :return:
        """
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
        response = {}
        if Account.create_account(first_name, last_name, user_name, email, date_of_birth, password, password_confirm):
            response['response'] =  "Account Created"
            return jsonify(response)
        else:
            response['response'] = "Account Creation Failed"
            return make_response(jsonify(response), 500)