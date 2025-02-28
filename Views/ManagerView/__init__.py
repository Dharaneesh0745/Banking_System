from Controllers.AccountController import AccountController
from Views.CustomerView.CustomerDisplay import CustomerDisplay
from Views.CustomerView.CustomerGetInput import CustomerGetInput
from Views.ManagerView.ManagerDisplay import ManagerDisplay
from Views.ManagerView.ManagerGetInput import ManagerGetInput
from Controllers.CustomerController import CustomerController

class ManagerView:

    def __init__(self, customer_controller: CustomerController, account_controller: AccountController):
        self.customer_controller = customer_controller
        self.account_controller = account_controller

    def main(self):

        while True:
            ManagerDisplay.manager_options()
            operation = ManagerGetInput.get_manager_operation()

            match operation:
                case 1:
                    customer_data = CustomerGetInput.get_customer_data()
                    self.customer_controller.create_customer_controller(customer_data)

                case 2:
                    phone_number = CustomerGetInput.get_customer_phone_number()
                    customer_data = self.customer_controller.get_customer_data(phone_number)
                    if not customer_data is None:
                        CustomerDisplay.account_type_options()
                        account_type = CustomerGetInput.get_account_type()

                        match account_type:
                            case 1:
                                self.account_controller.create_account_controller(customer_data, "Savings", 500.0)

                            case 2:
                                self.account_controller.create_account_controller(customer_data, "Current", 0.0)

                case 0:
                    return
