from Models.CustomerModel import Customer
from Schemas.AccountSchema import AccountSchema
from Services.AccountService import AccountService
import random
from datetime import date

class AccountController:

    def __init__(self, account_service: AccountService):
        self.account_service = account_service

    def create_account_controller(self, customer_data: Customer, account_type, balance):
        account_data = {"account_number": str(random.randint(1000000, 10000000)),
            "customer_id": customer_data.customer_id,
            "customer_phone_number": customer_data.phone_number,
            "account_type": account_type,
            "balance": balance,
            "date_opened": str(date.today()),
            "status": "Active"
        }
        account_schema = AccountSchema(**account_data)
        self.account_service.create_account(account_schema, account_type)

    # def get_all_my_accounts(self, phone_number):
    #     my_accounts = self.account_service.get_all_my_accounts(phone_number)
    #     return my_accounts if my_accounts else None
