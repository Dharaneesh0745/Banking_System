from Models.Accounts.AccountModel import Account

class CurrentAccount(Account):
    def __init__(self, account_data):
        super().__init__(account_data)
        self.overdraft_limit = 5000.00
        self.monthly_fee = 5.00

    def account_details(self):
        return f"{super().__str__()}, Overdraft Limit: {self.overdraft_limit}, Monthly Fee: {self.monthly_fee}"
