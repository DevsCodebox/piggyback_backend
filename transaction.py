from mongo_connection import client

class Transaction():
    @staticmethod
    def get_receipt(user_id, start, end):
        """
        Returns a list of dicts from the time period for a user

        :param user_id:
        :param start: must be int YYYYMMDD
        :param end: int YYYYMMDD
        :return:
        """
        transaction_db = client.transactions
        users_transactions_cursor = transaction_db.find({"user_id": user_id})
        user_transactions = [ i for i in users_transactions_cursor]
        transactions = []
        date_set = set()
        for i in range(start,end+1):
            date_set.add(i)
        for entry in user_transactions:
            if entry['start_time'] in date_set:
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
            "users_borrowing": 1,
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
            'users_borrowing': None,
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
