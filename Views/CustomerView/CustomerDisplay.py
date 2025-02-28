from Models.Accounts.CurrentAccountModel import CurrentAccount
from Models.Accounts.SavingsAccountModel import SavingsAccount
from Models.CustomerModel import Customer
from Schemas.AccountSchema import AccountSchema

class CustomerDisplay:

    @staticmethod
    def customer_created(customer: Customer):
        print("Customer created successfully!!!")
        print(customer)

    @staticmethod
    def customer_not_found():
        print("Customer not found in the database!!!")

    @staticmethod
    def account_type_options():
        print("\n*** Account type options ***")
        print("1. Savings Account - [1]")
        print("2. Current Account - [2]")

    @staticmethod
    def savings_account_created(account: SavingsAccount):
        if isinstance(account, SavingsAccount):
            print("Savings account created successfully!!!")
        elif isinstance(account, CurrentAccount):
            print("Current account created successfully!!!")
        print(account.account_details())

    @staticmethod
    def customer_options():
        print("\n*** Select Customer Operation ***")
        print("1. View all particular customer accounts")
        print("2. Check Balance")
        print("3. Deposit Amount")
        print("4. Withdraw Amount")
        print("0. Logout Customer")

    @staticmethod
    def account_not_found():
        print("Account not found, associated with this mobile number!!!")

    @staticmethod
    def display_my_accounts(my_accounts):

        for account in my_accounts:
            (
                account_id, account_number, customer_id, customer_phone_number, account_type,
                balance, date_opened, status, interest_rate, minimum_balance, overdraft_limit, monthly_fee
            ) = account

            account_data = AccountSchema(
                account_id=account_id,
                account_number=account_number,
                customer_id=customer_id,
                customer_phone_number=customer_phone_number,
                account_type=account_type,
                balance=balance,
                date_opened=date_opened,
                status=status,
                interest_rate=interest_rate,
                minimum_balance=minimum_balance,
                overdraft_limit=overdraft_limit,
                monthly_fee=monthly_fee
            )

            if account_type == "Savings":
                account_obj = SavingsAccount(account_data)
                print(account_obj)
            elif account_type == "Current":
                account_obj = CurrentAccount(account_data)
                print(account_obj)

    @staticmethod
    def display_account_balance(balance, account_number):
        print(f"Available balance: {balance} | Account number: {account_number}")

    @staticmethod
    def display_withdraw_amount_balance_status(balance, withdraw_amount):
        print(f"You have withdraw: {withdraw_amount}, remaining balance: {balance}")

    @staticmethod
    def minimum_balance_error(balance, minimum_balance):
        if minimum_balance != 0:
            print(f"You have balance of only: {balance}, with minimum balance: {minimum_balance}")
        else:
            print(f"You have balance of only: {balance}")

    @staticmethod
    def withdraw_amount_zero_error():
        print("Withdraw amount should be greater than zero.")

    @staticmethod
    def deposit_amount_zero_error():
        print("Deposit amount should be greater than zero.")

    @staticmethod
    def display_deposit_amount_balance_status(balance, deposit_amount):
        print(f"You have deposited amount: {deposit_amount}, Total balance: {balance}")
