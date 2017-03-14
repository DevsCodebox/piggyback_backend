from mongo_connection import client

class Transaction():
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
        for entry in users_transactions:
            if entry['start_time'] in date_set:
                ret.append(entry)
        return transactions


    def add_transaction(self, info):
        """

        :param list info: dict of info to insert
        :return: None
        """
        transaction_db = client.transactions
        for entry in info:
            transaction_db.insert_one(info)
