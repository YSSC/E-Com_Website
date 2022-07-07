class Inventory:

    def __init__(self,product,quantity,supplier,product_number,category,sub_category):
        self.product = product
        self.quantity = quantity
        self.supplier = supplier
        self.product_number = product_number
        self.order_status = "Delivering"
        self.category = category
        self.sub_category = sub_category

    def set_order_status(self,order_status):
        self.order_status = order_status

    def get_order_status(self):
        if self.quantity == 0:
            self.order_status = "Delivered"
        return self.order_status


class Warehouse(Inventory):
    count_id = 0

    def __init__(self,product,quantity,supplier,threshold,product_number,category,sub_category):
        Warehouse.count_id += 1
        super().__init__(product,quantity,supplier,product_number,category,sub_category)
        self.threshold = threshold
        self.__warehouse_id = Warehouse.count_id

    def set_warehouse_id(self,warehouse_id):
        self.__warehouse_id = warehouse_id

    def get_warehouse_id(self):
        return self.__warehouse_id


class Order(Inventory):
    count_id = 0

    def __init__(self,
                 product,
                 quantity,
                 product_number,
                 supplier,
                 category,
                 sub_category,
                 order_date,
                 delivery_date,
                 amount):
        Order.count_id += 1
        super().__init__(product,
                         quantity,
                         supplier,
                         product_number,
                         category,
                         sub_category)
        self.__order_id = Order.count_id
        self.__order_date = order_date
        self.__delivery_date = delivery_date
        self.__amount = amount

    def get_order_id(self):
        return self.__order_id

    def set_order_id(self,order_id):
        self.__order_id = order_id

    def set_order_date(self,order_date):
        self.__order_date = order_date

    def set_delivery_date(self,delivery_date):
        self.__delivery_date = delivery_date

    def set_amount(self,amount):
        self.__amount = amount

    def get_order_date(self):
        return self.__order_date

    def get_delivery_date(self):
        return self.__delivery_date

    def get_amount(self):
        return self.__amount

