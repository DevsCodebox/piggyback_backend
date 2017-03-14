from mongo_connection import client

class account():
    def get_user(self, user_id):
        user_db = client.user
        user = user_db.find({"user_id": user_id})
        return user[0]