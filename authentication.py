from mongo_connection import client

found_users = []

class Authentication:
    def check_login(self, user_name, password):
        users = client.users
        for user in users.find({"user_name": user_name, "password": password}):
            found_users.append(user)
	if (len(found_users) == 1):
            return user
	else:
	    return None
