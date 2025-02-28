from Database import Database
from Models.CustomerModel import Customer
from Exceptions.CustomerException import CustomerException

class CustomerDAO:

    def __init__(self, db: Database):
        self.db = db

    def add_customer_to_database(self, customer: Customer):
        query = """
            INSERT INTO customers (
                name, dob, city, pincode, phone_number, email, aadhar_number
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (customer.name, customer.dob, customer.city, customer.pincode, customer.phone_number, customer.email, customer.aadhar_number)

        try:
            self.db.execute(query, values)
            return True, customer
        except Exception as e:
            CustomerException.create_customer_exception(e)

    def fetch_customer_data(self, phone_number):
        query = "SELECT * FROM customers WHERE phone_number = %s"
        try:
            return self.db.fetchone(query, (phone_number,))
        except Exception as e:
            CustomerException.fetch_customer_exception(e)