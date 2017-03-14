from mongo_connection import client

class transaction():
    def get_receipt(self, user_id, start, end):
        """

        :param user_id:
        :param start: must be int YYYYMMDD
        :param end: int YYYYMMDD
        :return:
        """
        transaction_db = client.transactions
        users_transactions_cursor = transaction_db.find({"user_id": user_id})
        user_transactions = [ i for i in users_transactions_cursor]
        ret = []
        date_set = set()
        for i in range(start,end+1):
            date_set.add(i)
        for entry in users_transactions:
            if entry['start_time'] in date_set:
                ret.append(entry)

        return ret


