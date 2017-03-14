from mongo_connection import client
import json

class Connections():
	# function to return the max strength ssid from a list
	def strongest_ssid(self, ssid_list):
		connections = client.connections
		strongest = 0
		best_ssid = 0
		for ssid in ssid_list:
			for connection in connections.find({"ssid": ssid}):
				if connection.ssid_strength > strongest:
					strongest = connection.ssid_strength
					best_ssid = connection.ssid
				break

		return best_ssid

	def add_new_ssid(self, ssid, ssid_strength):
		connections = client.connections

		data = {}
		data['ssid'] = ssid
		data['ssid_strength'] = ssid_strength

		json_data = json.dumps(data)
		result = connections.insert_one(json_data)

		return True

	def update_ssid_strength(self, ssid, ssid_strength):
		connections = client.connections
		connections.update(
			{"ssid": ssid},
			{$set: {"ssid_strength": ssid_strength}}
		)