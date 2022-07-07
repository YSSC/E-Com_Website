class Register:

    def __init__(self, first_name, last_name, gender, email, phonenumber, dateofbirth):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__email = email
        self.__phonenumber = phonenumber
        self.__dateofbirth = dateofbirth

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phonenumber(self):
        return self.__phonenumber

    def set_phonenumber(self, phonenumber):
        self.__phonenumber = phonenumber

    def get_dateofbirth(self):
        return self.__dateofbirth

    def set_dateofbirth(self, dateofbirth):
        self.__dateofbirth = dateofbirth
