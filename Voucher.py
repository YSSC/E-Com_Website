class Voucher:
    count_id = 0

    def __init__(self,product_name,claimed,expiry, status, code):
        Voucher.count_id += 1
        self.__voucher_id = Voucher.count_id
        self.__product_name = product_name
        self.__claimed = claimed
        self.__expiry = expiry
        self.__status = status
        self.__code = code

    def get_voucher_id(self):
        return self.__voucher_id

    def get_product_name(self):
        return self.__product_name

    def get_claimed(self):
        return self.__claimed

    def get_expiry(self):
        return self.__expiry

    def get_status(self):
        return self.__status

    def get_code(self):
        return self.__code

    def set_voucher_id(self,voucher_id):
        self.__voucher_id = voucher_id

    def set_product_name(self,product_name):
        self.__product_name = product_name

    def set_claimed(self,claimed):
        self.__claimed = claimed

    def set_expiry(self,expiry):
        self.__expiry = expiry

    def set_status(self, status):
        self.__status = status

    def set_code(self, code):
        self.__code = code
