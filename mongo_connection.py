from pymongo import MongoClient

ADDRESS = 'localhost'
PORT = 27017
temp = MongoClient(ADDRESS, PORT)
client = temp.piggy
