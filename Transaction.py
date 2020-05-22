from datetime import date


class Transaction:

    transactions = []

    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date
        self.Add_Transaction()
    
    def Add_Transaction(self):
        self.transactions.append("{} {} {} {}".format(
            self.name, self.category, self.date, self.amount))


    def get_transac(self):
        return '{} \nType: {} \nDate: {} \nAmount: {}'.format(self.name, self.category, self.date, self.amount)
    
    def get_all_transc(self):
        for x in self.transactions:
            print(x)


trans_1 = Transaction("coop", 300, "food", date.today())
trans_2 = Transaction("willys", 1000, "food", date.today())
trans_3 = Transaction("lidl", 500, "food", date.today())
trans_4 = Transaction("tempo", 100, "food", date.today())

trans = Transaction()
# print(trans_1.get_transac())
trans.get_all_transc()

