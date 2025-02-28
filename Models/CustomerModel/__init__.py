from Schemas.CustomerSchema import CustomerSchema

class Customer:

    def __init__(self, customer_data: CustomerSchema):
        self.customer_id = customer_data.customer_id
        self.name = customer_data.name
        self.dob = customer_data.dob
        self.city = customer_data.city
        self.pincode = customer_data.pincode
        self.phone_number = customer_data.phone_number
        self.email = customer_data.email
        self.aadhar_number = customer_data.aadhar_number

    def __str__(self) -> str:
        return f"Customer [Name: {self.name}, DOB: {self.dob}, City: {self.city}, Pincode: {self.pincode}, Phone Number: {self.phone_number}, Email: {self.email}, Aadhar Number: {self.aadhar_number}]"
