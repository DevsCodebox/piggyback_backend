from pymongo import MongoClient

ADDRESS = 'some_string'
PORT = some_number
DB_URI = 'mongodb://' + ADDRESS + ':' + str(PORT)
client = MongoClient(DB_URI)
