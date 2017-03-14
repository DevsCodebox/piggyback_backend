#!flask/bin/python

"""Alternative version of the ToDo RESTful server implemented using the
Flask-RESTful extension."""
from login import Login
from addTransaction import AddTransaction
from getReceipt import GetReceipt
from changePassword import ChangePassword
from updateCredits import UpdateCredits
from updateSSIDStrength import UpdateSSIDStrength
from getStrongestSSID import GetStrongestSSID
from addNewSSID import AddNewSSID

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
api.add_resource(GetReceipt, 'api/receipt', endpoint='get_receipt'

api.add_resource(ChangePassword, 'api/changePassword', endpoint='change_password')
api.add_resource(UpdateCredits, 'api/updateCredits', endpoint='update_credits')

api.add_resource(UpdateSSIDStrength, 'api/updateSSIDStrength', endpoint='update_ssid_strength')
api.add_resource(GetStrongestSSID, 'api/getStrongestSSID', endpoint='get_strongest_ssid')
api.add_resource(AddNewSSID, 'api/addNewSSID', endpoint='add_new_ssid')


if __name__ == '__main__':
    app.run(debug=True)
