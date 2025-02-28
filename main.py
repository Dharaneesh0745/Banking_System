from Database import Database
from Views.ManagerView import ManagerView
from Controllers.CustomerController import CustomerController
from Services.CustomerService import CustomerService
from DAO.CustomerDAO import CustomerDAO
from Controllers.AccountController import AccountController
from Services.AccountService import AccountService
from DAO.AccountDAO import AccountDAO
# from Views.CustomerView import CustomerView
from Views.MainView.MainDisplay import MainDisplay
from Views.MainView.MainGetInput import MainGetInput

if __name__ == "__main__":

    db = Database()

    customer_dao = CustomerDAO(db)
    customer_service = CustomerService(customer_dao)
    customer_controller = CustomerController(customer_service)

    account_dao = AccountDAO(db)
    account_service = AccountService(account_dao)
    account_controller = AccountController(account_service)

    # customer_view = CustomerView(customer_controller, account_controller)
    manager_view = ManagerView(customer_controller, account_controller)

    while True:
        MainDisplay.authentication_options()
        authenticated_user = MainGetInput.get_authentication_role()

        match authenticated_user:
            case 1:
                # customer_view.main()
                pass
            case 2:
                manager_view.main()

            case 0:
                exit()
