from mongo_connection import client
import json

class Account():
	@staticmethod
	def get_user(user_name):
		user_db = client.users
		user = user_db.find_one({'user_name': user_name})
		return user

	@staticmethod
	def create_account(first_name, last_name, user_name, email, date_of_birth, password, password_confirm):
		"""
		curl -H "Content-Type: application/json" -X POST localhost:5000/api/createUser -d '{"first_name":"test2",
		 "last_name":"test", "email":"email",
        "date_of_birth":"temp",
        "password":"temp",
        "Password_confirm":"temp",
        "user_name":"wtf_a"}'

		:param first_name:
		:param last_name:
		:param user_name:
		:param email:
		:param date_of_birth:
		:param password:
		:param password_confirm:
		:return:
		"""
		# check for user_name already existing
		if Account.find_user(user_name):
			return False
		# check if password and password_confirm match
		if password != password_confirm:
			return False
		# then create the account
		data = {}
		data['first_name'] = first_name
		data['last_name'] = last_name
		data['user_name'] = user_name
		data['email'] = email
		data['date_of_birth'] = date_of_birth
		data['password'] = password
		data['credits'] = 0

		users = client.users

		users.insert_one(data)
		return True

	@staticmethod
	def find_user( user_name):
		users = client.users
		temp = users.find_one({'user_name': user_name})
		if temp:
			return True
		return False


	@staticmethod
	def change_password(user_name, old_password, new_password, password_confirm):
		if not Account.compare_passwords(new_password, password_confirm):
			return False
		users = client.users
		users.update(
			{'user_name': user_name},
			{'$set': {'password': new_password}}
		)
		return True

	@staticmethod
	def update_credits( user_name, credit_difference):
		users = client.users
		credit = 0

		user = users.find_one({'user_name': user_name})
		credit = user['credits'] + credit_difference

		users.update(
			{'user_name': user_name},
			{'$set': {'credits': credit}}
		)
		
		return True

