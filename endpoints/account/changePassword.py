from flask import jsonify, request, make_response
from flask.ext.restful import Resource, reqparse
from library.account import Account

class ChangePassword(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(ChangePassword, self).__init__()


    def post(self):
        """
        '{
        "user_name":"test",
        "password":"test2",
        "password_confirm":"test2"
        }'
        :return:
        """
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)
        user_name = data.get('user_name')
        password = data.get('password')
        prev_password = data.get('prev_password')
        password_confirm = data.get('password_confirm')
        if Account.change_password(user_name, prev_password, password, password_confirm):
            return jsonify({'response': 'ok'})
        else:
            return make_response(jsonify({'response': 'Bad Request'}), 500)
