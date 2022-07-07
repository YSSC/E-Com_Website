import Register


class User(Register.Register):
    count_id = 0

    def __init__(self, first_name, last_name, gender, email, phonenumber, dateofbirth, jobscope, password, confirmpassword, status):
        super().__init__(first_name, last_name, gender, email, phonenumber, dateofbirth)
        User.count_id +=1
        self.__user_id = User.count_id
        self.__jobscope = jobscope
        self.__status = status
        self.__password = password
        self.__confirmpassword = confirmpassword

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_jobscope(self):
        return self.__jobscope

    def set_jobscope(self, jobscope):
        self.__jobscope = jobscope

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
