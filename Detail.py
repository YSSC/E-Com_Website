import Product


class Detail(Product.Product):
    count_id = 0

    def __init__(self, brand, name, shade, number, price, description, category, sub, quantity):
        super().__init__(brand, name, shade, number, price, description, category, sub, quantity)
        Detail.count_id += 1
        self.__detail_id = Detail.count_id

    def get_detail_id(self):
        return self.__detail_id

    def set_detail_id(self, detail_id):
        self.__detail_id = detail_id
