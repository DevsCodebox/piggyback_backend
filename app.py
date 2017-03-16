#!flask/bin/python

"""Alternative version of the ToDo RESTful server implemented using the
Flask-RESTful extension."""

from flask import Flask, jsonify, make_response
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import Api
from getReceipt import GetReceipt
from updateCredits import UpdateCredits

from endpoints.account.changePassword import ChangePassword
from endpoints.account.createUser import CreateUser
from endpoints.account.login import Login

from endpoints.connections.addNewSSID import AddNewSSID
from endpoints.connections.getStrongestSSID import GetStrongestSSID
from endpoints.connections.updateSSIDStrength import UpdateSSIDStrength
from endpoints.connections.initConnection import InitConnection
from endpoints.connections.getBandwidthUsed import GetBandwidthUsed
from endpoints.connections.updateFriends import UpdateFriends

from endpoints.transaction.addTransaction import AddTransaction

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)
#Account
api.add_resource(Login, '/api/login', endpoint='login')
api.add_resource(CreateUser, '/api/createUser', endpoint='create_user')
api.add_resource(ChangePassword, '/api/changePassword', endpoint='change_password')
api.add_resource(UpdateCredits, '/api/updateCredits', endpoint='update_credits')

#connections
api.add_resource(UpdateSSIDStrength, '/api/updateSSIDStrength', endpoint='update_ssid_strength')
api.add_resource(GetStrongestSSID, '/api/getStrongestSSID', endpoint='get_strongest_ssid')
api.add_resource(AddNewSSID, '/api/addNewSSID', endpoint='add_new_ssid')
api.add_resource(InitConnection, '/api/initConnection', endpoint='init_connection')
api.add_resource(GetBandwidthUsed, '/api/getBandwidthUsed', endpoint='get_bandwidth_used')
api.add_resource(UpdateFriends, '/api/updateFriends', endpoint='update_friends')

#transaction
#authentication


api.add_resource(AddTransaction, '/api/transaction', endpoint='add_transaction')
api.add_resource(GetReceipt, '/api/receipt', endpoint='get_receipt')




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
