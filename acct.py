class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,dep_amt):
        self.balance = self.balance + dep_amt
        print('Added '+str(dep_amt)+' to the balance.')
    def withdraw(self,withdraw_amt):
        if self.balance - withdraw_amt < 0:
            print('not enough $$ in balance')
        else:
            self.balance = self.balance - withdraw_amt
            print('withdraw accepted')
    def __str__(self):
        return f"Owner: {self.owner} ; Balance: {self.balance}"

acct = Account("Dan",1000)

print(acct)
acct.deposit(1000)
acct.withdraw(2009)