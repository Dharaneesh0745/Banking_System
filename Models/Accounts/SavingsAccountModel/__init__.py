from Models.Accounts.AccountModel import Account

class SavingsAccount(Account):
    def __init__(self, account_data):
        super().__init__(account_data)
        self.interest_rate = 1.5
        self.minimum_balance = 500

    def account_details(self):
        return f"{super().__str__()}, Interest Rate: {self.interest_rate}%, Minimum Balance: {self.minimum_balance}"
