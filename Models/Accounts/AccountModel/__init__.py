from abc import ABC, abstractmethod
from Schemas.AccountSchema import AccountSchema

class Account(ABC):
    def __init__(self, account_data: AccountSchema):
        self.account_id = account_data.account_id
        self.account_number = account_data.account_number
        self.customer_id = account_data.customer_id
        self.customer_phone_number = account_data.customer_phone_number
        self.account_type = account_data.account_type
        self.balance = account_data.balance
        self.date_opened = account_data.date_opened
        self.status = account_data.status

    @abstractmethod
    def account_details(self):
        pass

    def __str__(self):
        return (f"Account [ID: {self.account_id}, Number: {self.account_number}, Type: {self.account_type}, "
                f"Balance: {self.balance}, Status: {self.status}]")