from typing import TYPE_CHECKING
from Views.CustomerView.CustomerDisplay import CustomerDisplay
from Views.CustomerView.CustomerGetInput import CustomerGetInput

if TYPE_CHECKING:
    from Controllers.CustomerController import CustomerController
    from Controllers.AccountController import AccountController

class CustomerView:
    def __init__(self, customer_controller: "CustomerController", account_controller: "AccountController"):
        self.customer_controller = customer_controller
        self.account_controller = account_controller

    def main(self):
        while True:
            CustomerDisplay.customer_options()
            operation = CustomerGetInput.get_customer_operation()

            match operation:
                case 1:
                    phone_number = CustomerGetInput.get_customer_phone_number()
                    my_accounts = self.account_controller.get_all_my_accounts(phone_number)
                    CustomerDisplay.display_my_accounts(my_accounts)

                case 2:
                    phone_number = CustomerGetInput.get_customer_phone_number()
                    my_accounts = self.account_controller.get_all_my_accounts(phone_number)
                    CustomerDisplay.display_my_accounts(my_accounts)
                    account_number = CustomerGetInput.get_customer_account_number()
                    my_balance = self.account_controller.get_account_balance(account_number)
                    CustomerDisplay.display_account_balance(my_balance, account_number)

                case 0:
                    return