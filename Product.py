class Product:
    count_id = 0

    def __init__(self, brand, name, shade, number, price, description, category, sub, quantity):
        Product.count_id += 1
        self.__product_id = Product.count_id
        self.__brand = brand
        self.__name = name
        self.__shade = shade
        self.__number = number
        self.__price = price
        self.__description = description
        self.__category = category
        self.__sub = sub
        self.__quantity = quantity

    def get_product_id(self):
        return self.__product_id

    def get_brand(self):
        return self.__brand

    def get_name(self):
        return self.__name

    def get_shade(self):
        return self.__shade

    def get_number(self):
        return self.__number

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def get_category(self):
        return self.__category

    def get_sub(self):
        return self.__sub

    def get_quantity(self):
        return self.__quantity

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_brand(self, brand):
        self.__brand = brand

    def set_name(self, name):
        self.__name = name

    def set_shade(self, shade):
        self.__shade = shade

    def set_number(self, number):
        self.__number = number

    def set_price(self, price):
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_category(self, category):
        self.__category = category

    def set_sub(self, sub):
        self.__sub = sub

    def set_quantity(self, quantity):
        self.__quantity = quantity

