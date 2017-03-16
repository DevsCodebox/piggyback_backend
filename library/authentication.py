from tools.mongo_connection import client

class Authentication:
    @staticmethod
    def check_login(user_name, password):
        users = client.users
        user = users.find_one({"user_name": user_name, "password": password})
        if user:
            return True
        return False
