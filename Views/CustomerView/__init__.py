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

                case 3:
                    phone_number = CustomerGetInput.get_customer_phone_number()
                    my_accounts = self.account_controller.get_all_my_accounts(phone_number)
                    CustomerDisplay.display_my_accounts(my_accounts)
                    account_number = CustomerGetInput.get_customer_account_number()
                    deposit_amount = CustomerGetInput.get_deposit_amount()

                    if deposit_amount  == 0:
                        CustomerDisplay.deposit_amount_zero_error()
                        continue

                    balance = self.account_controller.deposit_amount_to_account(account_number, deposit_amount)
                    if balance:
                        CustomerDisplay.display_deposit_amount_balance_status(balance, deposit_amount)

                case 4:
                    phone_number = CustomerGetInput.get_customer_phone_number()
                    my_accounts = self.account_controller.get_all_my_accounts(phone_number)
                    CustomerDisplay.display_my_accounts(my_accounts)
                    account_number = CustomerGetInput.get_customer_account_number()
                    withdraw_amount = CustomerGetInput.get_withdraw_amount()

                    if withdraw_amount == 0:
                        CustomerDisplay.withdraw_amount_zero_error()
                        continue

                    balance = self.account_controller.withdraw_amount_from_account(account_number, withdraw_amount)
                    if balance:
                        CustomerDisplay.display_withdraw_amount_balance_status(balance, withdraw_amount)

                case 0:
                    return