class AccountException:

    @staticmethod
    def create_account_exception(e):
        print("Error occurred while inserting new account: ", e)

    @staticmethod
    def fetch_account_exception(e):
        print("Error occurred while fetching account: ", e)
