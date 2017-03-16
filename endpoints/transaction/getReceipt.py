import json

from flask import jsonify, request, make_response
from flask.ext.restful import Resource, reqparse
from library.transaction import Transaction


class GetReceipt(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(GetReceipt, self).__init__()


    def post(self):
        """
        '{"user_name":"test",
        "start":epochtime,
        "end":epochtime...
        }']=

        '{"start_time": 1458112324472, "user_name": "a", "end_time": 1489648324472}'
        :return:
        """
        data = request.get_json()
        if not data:
            data = {"response": "Bad Request"}
            return jsonify(data)
        user_name = data.get('user_name')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        print(data)
        receipt = Transaction.get_receipt(user_name, start_time, end_time)
        print(receipt)
        if receipt:
            return json.dumps(receipt)
        else:
            data = {"response": "No Receipt"}
            return make_response(jsonify(data), 500)