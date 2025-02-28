# from Controllers.CustomerController import CustomerController
# from Controllers.AccountController import AccountController
# from Views.CustomerView.CustomerDisplay import CustomerDisplay
# from Views.CustomerView.CustomerGetInput import CustomerGetInput
#
# class CustomerView:
#
#     def __init__(self, customer_controller: CustomerController, account_controller: AccountController):
#         self.account_controller = account_controller
#         self.customer_controller = customer_controller
#
#     def main(self):
#
#         while True:
#             CustomerDisplay.customer_options()
#             operation = CustomerGetInput.get_customer_operation()
#
#             match operation:
#                 case 1:
#                     phone_number = CustomerGetInput.get_customer_phone_number()
#                     # my_accounts = self.account_controller.get_all_my_accounts(phone_number)
#                     # CustomerDisplay.display_my_accounts(my_accounts)
#
#                 case 2:
#                     pass
#
#                 case 3:
#                     pass
#
#                 case 4:
#                     pass
#
#                 case 0:
#                     return