import Register


class Customer(Register.Register):
    count_id = 0

    def __init__(self, first_name, last_name, gender, email, phonenumber, dateofbirth, date_joined, membership, address, password, confirmpassword, status):
        super().__init__(first_name, last_name, gender, email, phonenumber, dateofbirth)
        Customer.count_id += 1
        self.__customer_id = Customer.count_id
        self.__date_joined = date_joined
        self.__membership = membership
        self.__address = address
        self.__status = status
        self.__password = password
        self.__confirmpassword = confirmpassword

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_date_joined(self):
        return self.__date_joined

    def set_date_joined(self, date_joined):
        self.__date_joined = date_joined

    def get_membership(self):
        return self.__membership

    def set_membership(self, membership):
        self.__membership = membership

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_confirmpassword(self):
        return self.__confirmpassword

    def set_confirmpassword(self, confirmpassword):
        self.__confirmpassword = confirmpassword

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

