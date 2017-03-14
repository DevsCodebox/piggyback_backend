from mongo_connection import client

class Account():
    def get_user(self, user_id):
        user_db = client.user
        user = user_db.find_one({"user_id": user_id})
        return user