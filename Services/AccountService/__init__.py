from DAO.AccountDAO import AccountDAO
from Models.Accounts.CurrentAccountModel import CurrentAccount
from Models.Accounts.SavingsAccountModel import SavingsAccount
from Schemas.AccountSchema import AccountSchema
from Views.CustomerView.CustomerDisplay import CustomerDisplay

class AccountService:

    def __init__(self, account_dao: AccountDAO):
        self.account_dao = account_dao

    def create_account(self, account_schema: AccountSchema, account_type):
        new_account = None
        if account_type == "Savings":
            new_account = SavingsAccount(account_schema)
        elif account_type == "Current":
            new_account = CurrentAccount(account_schema)
        result, account = self.account_dao.add_account_to_database(new_account)
        if result:
            CustomerDisplay.savings_account_created(account)

    # def get_all_my_accounts(self, phone_number):
    #     my_accounts = self.account_dao.fetch_all_my_accounts(phone_number)
    #
    #     if not my_accounts:
    #         CustomerDisplay.account_not_found()
    #         return None
    #     return my_accounts