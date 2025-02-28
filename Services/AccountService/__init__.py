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

    def get_all_my_accounts(self, phone_number):
        my_accounts = self.account_dao.fetch_all_my_accounts(phone_number)

        if not my_accounts:
            CustomerDisplay.account_not_found()
            return None
        return my_accounts

    def get_account_balance(self, account_number):
        my_balance = self.account_dao.get_account_balance_from_db(account_number)

        if not my_balance:
            CustomerDisplay.account_not_found()
            return None
        return my_balance

    def withdraw_amount_from_account(self, account_number, withdraw_amount):
        my_account = self.account_dao.fetch_one_account(account_number)

        if my_account:
            account_id, account_number, customer_id, customer_phone_number, account_type, balance, date_opened, status, interest_rate, minimum_balance, overdraft_limit, monthly_fee = my_account
            account_schema = AccountSchema(account_id=account_id, account_number=account_number, customer_id=customer_id, customer_phone_number=customer_phone_number, account_type=account_type, balance=balance, date_opened=date_opened, status=status, interest_rate=interest_rate, minimum_balance=minimum_balance, overdraft_limit=overdraft_limit, monthly_fee=monthly_fee)

            if account_type == "Savings":
                account = SavingsAccount(account_schema)
                if account.balance - withdraw_amount >= account.minimum_balance:
                    new_balance = account.balance - withdraw_amount
                    self.account_dao.withdraw_amount_from_db(account_number, new_balance)
                    return new_balance
                else:
                    CustomerDisplay.minimum_balance_error(account.balance, account.minimum_balance)

            elif account_type == "Current":
                account = CurrentAccount(account_schema)
                if account.balance - withdraw_amount >= 0:
                    new_balance = account.balance - withdraw_amount
                    self.account_dao.withdraw_amount_from_db(account_number, new_balance)
                    return new_balance
                else:
                    CustomerDisplay.minimum_balance_error(account.balance, 0)

        else:
            CustomerDisplay.account_not_found()
            return None

    def deposit_amount_to_account(self, account_number, deposit_amount):
        my_account = self.account_dao.fetch_one_account(account_number)

        if my_account:
            account_id, account_number, customer_id, customer_phone_number, account_type, balance, date_opened, status, interest_rate, minimum_balance, overdraft_limit, monthly_fee = my_account
            account_schema = AccountSchema(account_id=account_id, account_number=account_number, customer_id=customer_id, customer_phone_number=customer_phone_number, account_type=account_type, balance=balance, date_opened=date_opened, status=status, interest_rate=interest_rate, minimum_balance=minimum_balance, overdraft_limit=overdraft_limit, monthly_fee=monthly_fee)

            if account_type == "Savings":
                account = SavingsAccount(account_schema)
                new_balance = account.balance + deposit_amount
                self.account_dao.deposit_amount_to_account_in_db(account_number, new_balance)
                return new_balance

            elif account_type == "Current":
                account = CurrentAccount(account_schema)
                new_balance = account.balance + deposit_amount
                self.account_dao.deposit_amount_to_account_in_db(account_number, new_balance)
                return new_balance

        else:
            CustomerDisplay.account_not_found()
            return None