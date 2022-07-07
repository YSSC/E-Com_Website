class Card:
    count_id = 0

    def __init__(self, cname, cnum, expiry, cvv, address, city, state, postalcode):
        Card.count_id += 1
        self.__card_id = Card.count_id
        self.__cname = cname
        self.__cnum = cnum
        self.__expiry = expiry
        self.__cvv = cvv
        self.__address = address
        self.__city = city
        self.__state = state
        self.__postalcode = postalcode

    def get_card_id(self):
        return self.__card_id

    def set_card_id(self, card_id):
        self.__card_id = card_id

    def get_cname(self):
        return self.__cname

    def set_cname(self, cname):
        self.__cname = cname

    def get_cnum(self):
        return self.__cnum

    def set_cnum(self, cnum):
        self.__cnum = cnum

    def get_expiry(self):
        return self.__expiry

    def set_expiry(self, expiry):
        self.__expiry = expiry

    def get_cvv(self):
        return self.__cvv

    def set_cvv(self, cvv):
        self.__cvv = cvv

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    def get_postalcode(self):
        return self.__postalcode

    def set_postalcode(self, postalcode):
        self.__postalcode = postalcode
