#!flask/bin/python

"""Alternative version of the ToDo RESTful server implemented using the
Flask-RESTful extension."""

from endpoints.account.changePassword import ChangePassword
from endpoints.account.getStrongestSSID import GetStrongestSSID
from endpoints.account.updateSSIDStrength import UpdateSSIDStrength
from flask import Flask, jsonify, make_response
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import Api
from getReceipt import GetReceipt
from updateCredits import UpdateCredits

from endpoints.account.createUser import CreateUser
from endpoints.connections.addNewSSID import AddNewSSID
from endpoints.transaction.addTransaction import AddTransaction
from library.login import Login

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)

api.add_resource(Login, '/api/login', endpoint='login')

api.add_resource(AddTransaction, '/api/transaction', endpoint='add_transaction')
api.add_resource(GetReceipt, '/api/receipt', endpoint='get_receipt')

api.add_resource(CreateUser, '/api/createUser', endpoint='create_user')
api.add_resource(ChangePassword, '/api/changePassword', endpoint='change_password')
api.add_resource(UpdateCredits, '/api/updateCredits', endpoint='update_credits')

api.add_resource(UpdateSSIDStrength, '/api/updateSSIDStrength', endpoint='update_ssid_strength')
api.add_resource(GetStrongestSSID, '/api/getStrongestSSID', endpoint='get_strongest_ssid')
api.add_resource(AddNewSSID, '/api/addNewSSID', endpoint='add_new_ssid')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
