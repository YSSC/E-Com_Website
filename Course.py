class Course:

    def __init__(self, course_name, course_description, course_instructor, course_date, course_time, course_duration, course_status):
        self.__course_name = course_name
        self.__course_description = course_description
        self.__course_instructor = course_instructor
        self.__course_date = course_date
        self.__course_time = course_time
        self.__course_duration = course_duration
        self.__course_status = course_status

    def get_course_name(self):
        return self.__course_name

    def set_course_name(self, course_name):
        self.__course_name = course_name

    def get_course_description(self):
        return self.__course_description

    def set_course_description(self, course_description):
        self.__course_description = course_description

    def get_course_instructor(self):
        return self.__course_instructor

    def set_course_instructor(self, course_instructor):
        self.__course_duration = course_instructor

    def get_course_date(self):
        return self.__course_date

    def set_course_date(self, course_date):
        self.__course_date = course_date

    def get_course_time(self):
        return self.__course_time

    def set_course_time(self, course_time):
        self.__course_time = course_time

    def get_course_duration(self):
        return self.__course_duration

    def set_course_duration(self, course_duration):
        self.__course_duration = course_duration

    def get_course_status(self):
        return self.__course_status

    def set_course_status(self, course_status):
        self.__course_status = course_status
