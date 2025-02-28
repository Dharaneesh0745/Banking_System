from DAO.CustomerDAO import CustomerDAO
from Schemas.CustomerSchema import CustomerSchema
from Models.CustomerModel import Customer
from Views.CustomerView.CustomerDisplay import CustomerDisplay

class CustomerService:

    def __init__(self, customer_dao: CustomerDAO):
        self.customer_dao = customer_dao

    def create_customer(self, customer_schema: CustomerSchema):
        new_customer = Customer(customer_schema)
        result, customer = self.customer_dao.add_customer_to_database(new_customer)
        if result and customer:
            CustomerDisplay.customer_created(customer)

    def get_customer_data(self, phone_number):
        customer_data = self.customer_dao.fetch_customer_data(phone_number)

        if not customer_data:
            CustomerDisplay.customer_not_found()
            return None

        customer_id, name, dob, city, pincode, phone_number, email, aadhar_number = customer_data
        return CustomerSchema(customer_id=customer_id, name=name, dob=dob, city=city, pincode=pincode, phone_number=phone_number, email=email, aadhar_number=aadhar_number)
