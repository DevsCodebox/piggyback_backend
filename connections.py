from mongo_connection import client
import json

class Connections():
	# function to return the max strength ssid from a list
	@staticmethod
	def strongest_ssid(ssid_list):
		connections = client.connections
		strongest = 0
		best_ssid = 0
		for ssid in ssid_list:
			connection = connections.find_one({'ssid': ssid})
			if connection['ssid_strength'] > strongest:
				strongest = connection['ssid_strength']
				best_ssid = connection['ssid']
		return best_ssid

	@staticmethod
	def add_new_ssid(ssid, ssid_strength):
		connections = client.connections

		data = {}
		data['ssid'] = ssid
		data['ssid_strength'] = ssid_strength
		temp = connections.find_one({'ssid': ssid})
		if temp:
			return False

		connections.insert_one(data)

		return True

	@staticmethod
	def update_ssid_strength(ssid, ssid_strength):
		connections = client.connections

		connections.update(
			{'ssid': ssid},
			{'$set': {'ssid_strength': ssid_strength}}
		)

		return True
