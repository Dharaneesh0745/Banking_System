class CustomerException:

    @staticmethod
    def create_customer_exception(e):
        print("Error occurred while inserting new customer: ", e)

    @staticmethod
    def fetch_customer_exception(e):
        print("Error occurred while fetching customer: ", e)
