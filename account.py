from mongo_connection import client
import json

class Account():
	def get_user(self, user_id):
		user_db = client.user
		user = user_db.find_one({"user_id": user_id})
		return user
	
	def create_account(self, first_name, last_name, user_name, email, date_of_birth, password, password_confirm):
		# check for user_name already existing
		if self.find_user(user_name):
			return False
		# check if password and password_confirm match
		if not self.compare_passwords(password, password_confirm):
			return False
		# then create the account
		data = {}
		data['first_name'] = first_name
		data['last_name'] = last_name
		data['user_name'] = user_name
		data['email'] = email
		data['date_of_birth'] = date_of_birth
		data['password'] = password
		
		json_data = json.dumps(data)
		users = client.users

		result = users.insert_one(json_data)
		return True

	def find_user(self, user_name):
		users = client.users
		for user in users.find({"user_name": user_name}):
			return True
		return False

	def compare_passwords(self, password, password_confirm):
		if (password != password_confirm):
			return False
		return True

	def change_password(self, user_name, old_password, new_password, password_confirm):
		if not compare_passwords(new_password, password_confirm):
			return False
		users = client.users
		users.update(
			{"user_name": user_name},
				{$set: "password": new_password}
			}
		)
	
		return True
