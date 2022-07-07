class Supplier:
    count_id = 0

    def __init__(self, supplier,name, email, contact_no, address, country, postal_code, bank, bank_acc,status):
        Supplier.count_id += 1
        self.__supplier_id = Supplier.count_id
        self.__supplier = supplier
        self.__name = name
        self.__email = email
        self.__contact_no = contact_no
        self.__address = address
        self.__country = country
        self.__postal_code = postal_code
        self.__bank = bank
        self.__bank_acc = bank_acc
        self.__status = status

    def set_supplier_id(self,supplier_id):
        self.__supplier_id = supplier_id

    def set_supplier(self,supplier):
        self.__supplier = supplier

    def set_name(self,name):
        self.__name = name

    def set_email(self,email):
        self.__email = email

    def set_contact_no(self,contact_no):
        self.__contact_no = contact_no

    def set_address(self,address):
        self.__address = address

    def set_country(self,country):
        self.__country = country

    def set_postal_code(self,postal_code):
        self.__postal_code = postal_code

    def set_bank(self,bank):
        self.__bank = bank

    def set_bank_acc(self,bank_acc):
        self.__bank_acc = bank_acc

    def set_status(self, status):
        self.__status = status

    def get_supplier_id(self):
        return self.__supplier_id

    def get_supplier(self):
        return self.__supplier

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_contact_no(self):
        return self.__contact_no

    def get_address(self):
        return self.__address

    def get_country(self):
        return self.__country

    def get_postal_code(self):
        return self.__postal_code

    def get_bank(self):
        return self.__bank

    def get_bank_acc(self):
        return self.__bank_acc

    def get_status(self):
        return self.__status
