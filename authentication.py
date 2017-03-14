from mongo_connection import client

class Authentication:
    def check_login(self, user_name, password):
        users = client.users
        for user in users.find({"user_name": user_name, "password": password}):
            return user
	return None
