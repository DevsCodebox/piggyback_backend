from flask import jsonify, request, make_response
from flask.ext.restful import Resource, reqparse

from library.account import Account


class UpdateCredits(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(UpdateCredits, self).__init__()


    def post(self):
        """
        '{"credit_difference": 12, "user_name":"test"}'
        :return:
        """
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)
        credit_difference = data.get('credit_difference')
        user_name = data.get('user_name')
        response = {}
        if Account.update_credits(user_name, credit_difference):
            response['response'] = 'Credits updated'
            return jsonify(response)
        else:
            response['response'] = 'Credit Update Failed'
            return make_response(jsonify(response))