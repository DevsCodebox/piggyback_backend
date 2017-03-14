from mongo_connection import client

class Transaction():
    def __init__(self):
        self.template_transaction = {
            'transaction_type': None,
            'data_type': None,
            'start_time': None,
            'end_time': None,
            'data_usage': None,
            'credit_usage': None,
            'users_borrowing': None
        }


    def get_receipt(self, user_id, start, end):
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
                ret.append(entry)
        return transactions


    def add_transaction(self, info):
        """

        :param dict info: dict of info to insert
        :return: None
        """
        transaction_db = client.transactions
        data = {}
        for k,v in self.template_transaction.items():
            if k in info:
                data[k] = info[k]
            else:
                data[k] = v

        for entry in info:
            transaction_db.insert_one(data)
