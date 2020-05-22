from datetime import date


class Transaction:

    transactions = []
    trans_id = 0

    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date
        self.Add_Transaction()


    def Add_Transaction(self):
        Transaction.trans_id += 1
        Transaction.transactions.append("id:{}, {} {} {} {}".format(self.trans_id, self.name, self.category, self.amount, self.date))



    def get_all_transc():
        for x in Transaction.transactions:
            print(x)


trans_1 = Transaction("coop", 300, "food", date.today())
trans_2 = Transaction("willys", 1000, "food", date.today())
trans_3 = Transaction("lidl", 500, "food", date.today())
trans_4 = Transaction("tempo", 100, "food", date.today())

# print(trans_1.get_transac())
Transaction.get_all_transc()

