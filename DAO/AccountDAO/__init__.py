from Database import Database
from Models.Accounts.CurrentAccountModel import CurrentAccount
from Models.Accounts.SavingsAccountModel import SavingsAccount
from Exceptions.AccountException import AccountException

class AccountDAO:

    def __init__(self, db: Database):
        self.db = db

    def add_account_to_database(self, account: SavingsAccount):
        query = values = None
        if isinstance(account, SavingsAccount):
            query = """
                INSERT INTO accounts (
                    account_number, customer_id, customer_phone_number, account_type, balance, date_opened, status, interest_rate, minimum_balance
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (account.account_number, account.customer_id, account.customer_phone_number, account.account_type, account.balance, account.date_opened, account.status, account.interest_rate, account.minimum_balance)

        elif isinstance(account, CurrentAccount):
            query = """
                INSERT INTO accounts (
                    account_number, customer_id, customer_phone_number, account_type, balance, date_opened, status, overdraft_limit, monthly_fee
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (account.account_number, account.customer_id, account.customer_phone_number, account.account_type, account.balance, account.date_opened, account.status, account.overdraft_limit, account.monthly_fee)

        try:
            self.db.execute(query, values)
            return True, account
        except Exception as e:
            AccountException.create_account_exception(e)

    def fetch_all_my_accounts(self, phone_number):
        query = "SELECT * FROM accounts WHERE customer_phone_number = %s"
        try:
            return self.db.fetchall(query, (phone_number,))
        except Exception as e:
            AccountException.fetch_account_exception(e)

    def fetch_one_account(self, account_number):
        query = "SELECT * FROM accounts WHERE account_number = %s"
        try:
            return self.db.fetchone(query, (account_number,))
        except Exception as e:
            AccountException.fetch_account_exception(e)

    def get_account_balance_from_db(self, account_number):
        query = "SELECT balance from accounts WHERE account_number = %s"
        try:
            return self.db.fetchone(query, (account_number,))
        except Exception as e:
            AccountException.fetch_account_exception(e)

    def withdraw_amount_from_db(self, account_number, new_balance):
        query = "UPDATE accounts SET balance = %s WHERE account_number = %s"
        values = (new_balance, account_number)
        try:
            self.db.execute(query, values)
            return True
        except Exception as e:
            AccountException.fetch_account_exception(e)