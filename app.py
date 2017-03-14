#!flask/bin/python

"""Alternative version of the ToDo RESTful server implemented using the
Flask-RESTful extension."""
from login import Login
from addTransaction import AddTransaction
from getReceipt import GetReceipt

from flask import Flask, jsonify, abort, make_response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)

api.add_resource(Login, '/api/login', endpoint='login')
api.add_resource(AddTransaction, 'api/transaction', endpoint='add_transaction')
api.add_resource(GetReceipt, 'api/receipt', endpoint='get_receipt')

if __name__ == '__main__':
    app.run(debug=True)
