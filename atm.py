class ATM(object):

    def __init__(self, value=0):
        self.result = value

    def reset(self):
        self.result = 0

    def cash(self, account, cash):
        fee = 1
        max_cash = 2000
        total = cash + fee
        if cash < 0:
            self.result = 0
        elif cash >= max_cash:
            self.result = 0
        elif account < total:
            self.result = 0
        else:
            self.result = cash
        return self.result
