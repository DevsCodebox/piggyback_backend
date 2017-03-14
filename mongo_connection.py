from pymongo import MongoClient

ADDRESS = 'some_string'
PORT = some_number
DB_URI = 'mongodb://' + ADDRESS + ':' + PORT

def get_connection_info():
    client = MongoClient(DB_URI)
    return client
