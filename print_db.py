from pymongo import MongoClient

ADDRESS = 'localhost'
PORT = 27017
temp = MongoClient(ADDRESS, PORT)
client = temp.piggy
users = client.users
all_items = users.find()
print('\n\nusers\n\n')
for i in all_items:
    print (i)

print('\n\nconnections\n\n')
connections = client.connections
rows = connections.find()
for i in rows:
    print(i)

print('\n\ntransactions\n\n')
transactions = client.transactions
rows = transactions.find()
for i in rows:
    print(i)
