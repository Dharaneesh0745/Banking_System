from Services.CustomerService import CustomerService
from Schemas.CustomerSchema import CustomerSchema
from Models.CustomerModel import Customer

class CustomerController:

    def __init__(self, customer_service: CustomerService):
        self.customer_service = customer_service

    def create_customer_controller(self, customer_data):
        customer_schema = CustomerSchema(**customer_data)
        self.customer_service.create_customer(customer_schema)

    def get_customer_data(self, phone_number):
        customer_schema = self.customer_service.get_customer_data(phone_number)
        return Customer(customer_schema) if customer_schema else None