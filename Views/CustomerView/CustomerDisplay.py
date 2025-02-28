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
