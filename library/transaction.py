import time

from tools.mongo_connection import client
from library.connections import Connections
from library.account import Account

class Transaction():
    @staticmethod
    def get_receipt(user_name, start, end):
        """
        Returns a list of dicts from the time period for a user

        :param user_name:
        :param start: must be epoch
        :param end: epoch int
        :return:
        """
        transaction_db = client.transactions
        users_transactions_cursor = transaction_db.find({"user_name": user_name})
        print(users_transactions_cursor)
        user_transactions = [ i for i in users_transactions_cursor]
        transactions = []
        for entry in user_transactions:
            cur_start = entry['start_time']
            if start < cur_start < end:
                entry.pop('_id')
                transactions.append(entry)
        return transactions

    @staticmethod
    def add_transaction(info):
        """
        template_transaction = {
            "transaction_type": "test",
            "data_type": "test",
            "start_time": 20170313,
            "end_time": 20170314,
            "data_usage": 12,
            "credit_usage": 31,
            "user_name":"test"
        }
        :param dict info: dict of info to insert
        :return: None
        """
        template_transaction = {
            'transaction_type': None,
            'data_type': None,
            'start_time': None,
            'end_time': None,
            'data_usage': None,
            'credit_usage': None,
            'user_name': None
        }
        transaction_db = client.transactions
        data = {}
        for k,v in template_transaction.items():
            if k in info:
                data[k] = info[k]
            else:
                data[k] = v

        transaction_db.insert_one(data)
        client_info = Account.get_user(data['user_name'])
        #
        # data['transaction_type'] = 'host'
        #
        # data['user_name'] = info['host']
        # transaction_db.insert_one(data)
        return client_info['credits']


    @staticmethod
    def client_polling_update(ssid, user_name, credit, bandwidth):

        friends = Connections.get_friends(ssid) or []

        if user_name not in friends:
            Account.update_credits(user_name, -credit)
            Connections.update_credits(ssid, credit)
            host_name = Connections.get_user_name(ssid)
            if host_name:
                Account.update_credits(host_name, credit)

        Connections.update_bandwidth(ssid, bandwidth)

        credits_left = Account.get_user(user_name)['credits']

        return credits_left
