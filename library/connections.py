from tools.mongo_connection import client


class Connections():
    # function to return the max strength ssid from a list
    @staticmethod
    def strongest_ssid(ssid_list):
        connections = client.connections
        strongest = 0
        best_ssid = 0
        for ssid in ssid_list:
            connection = connections.find_one({'ssid': ssid})
            if connection['ssid_strength'] >= strongest:
                strongest = connection['ssid_strength']
                best_ssid = connection['ssid']
        return best_ssid

    @staticmethod
    def add_new_ssid(user_name, ssid, ssid_strength, friends):
        connections = client.connections

        data = {}
        data['user_name'] = user_name
        data['ssid'] = ssid
        data['ssid_strength'] = ssid_strength
        data['friends'] = friends
        data['bandwidth'] = 0
        data['credits'] = 0
        temp = connections.find_one({'ssid': ssid})
        if temp:
            return False

        connections.insert_one(data)

        return True

    @staticmethod
    def update_ssid_strength(ssid, ssid_strength):
        """
        :param ssid:
        :param ssid_strength: int Larger = better.
        :return:
        """
        connections = client.connections

        connections.update(
            {'ssid': ssid},
            {'$set': {'ssid_strength': ssid_strength}}
        )

        return True

    @staticmethod
    def update_friends(ssid, friends):
        connections = client.connections
        row = connections.find_one({'ssid': ssid})
        if not row:
            return False
        connections.update(
            {'ssid': ssid},
            {'$set': {'friends': [] }}
        )
        connections.update(
            {'ssid': ssid},
            {'$push': {'friends': {'$each': friends}}}
        )
        return True

    @staticmethod
    def get_friends(ssid):
        connections = client.connections
        row = connections.find_one({'ssid': ssid})
        friends = row['friends']
        return friends

    @staticmethod
    def update_bandwidth(ssid, bandwidth_difference):
        """
        always going to be going up.
        :param ssid:
        :param bandwidth_difference:
        :return:
        """
        connections = client.connections
        row = connections.find_one({'ssid': ssid})
        bandwidth = row['bandwidth'] + bandwidth_difference
        connections.update(
            {'ssid': ssid},
            {'$set': {'bandwidth': bandwidth}}
        )
        return True

    @staticmethod
    def update_credits(ssid, credit_difference):
        """
        always going up. credits used = credits gained
        :param ssid:
        :param credit_difference:
        :return:
        """
        connections = client.connections
        row = connections.find_one({'ssid': ssid})
        credit = row['credits'] + credit_difference
        connections.update(
            {'ssid': ssid},
            {'$set': {'credits': credit}}
        )
        return True

    @staticmethod
    def init_connections(ssid):
        """
        returns previous set ssid, sets credits and bandwidth to 0
        :param ssid:
        :return: bool
        """
        connections = client.connections
        row = connections.find_one({'ssid': ssid})
        if row:
            connections.update(
                {'ssid': ssid},
                {'$set': {'bandwidth': 0, 'credits': 0}}
            )

            return True
        else:
            return False

    @staticmethod
    def get_bandwidth_used(ssid):
        """
        returns the bandwidth used on a ssid
        :param ssid:
        :return:
        """
        connections = client.connections
        row = connections.find_one({'ssid': ssid})
        if row:
            return row['bandwidth']
        else:
            return False

    @staticmethod
    def get_user_name(ssid):
        """
        returns the user_name associated withe host of the ssid
        :param ssid:
        :return:
        """
        connections = client.connections
        row = connections.find_one({'ssid': ssid})
        return row['user_name']