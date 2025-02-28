class CustomerGetInput:

    @staticmethod
    def get_customer_data():
        # return {
        #     "name": input("Enter name: "),
        #     "dob": input("Enter DOB [YYYY-MM-DD]: "),
        #     "city": input("Enter city: "),
        #     "pincode": input("Enter pincode: "),
        #     "phone_number": input("Enter phone number: "),
        #     "email": input("Enter email: "),
        #     "aadhar_number": input("Enter Aadhar number: ")
        # }

        return {
            "name": "Dharaneesh",
            "dob": "2005-04-07",
            "city": "Coimbatore",
            "pincode": "641016",
            "phone_number": "9159883009",
            "email": "dharaneesh0745@gmail.com",
            "aadhar_number": "987654321000"
        }

    @staticmethod
    def get_customer_phone_number():
        return input("Enter customer phone number: ")

    @staticmethod
    def get_account_type():
        return int(input("Enter account type: "))

    @staticmethod
    def get_customer_operation():
        return int(input("Enter customer operation: "))

    @staticmethod
    def get_customer_account_number():
        return input("Enter account number: ")