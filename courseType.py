import Course


class Online(Course.Course):
    count_id = 0

    def __init__(self, course_name, course_instructor, course_date, course_time, course_duration, course_link, course_status, course_description):
        super().__init__(course_name, course_instructor, course_date, course_time, course_duration, course_status, course_description)
        Online.count_id += 1
        self.__course_id = Online.count_id
        self.__course_link = course_link

    def get_course_id(self):
        return self.__course_id

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def get_course_link(self):
        return self.__course_link

    def set_course_link(self, course_link):
        self.__course_link = course_link


class Offline(Course.Course):
    count_id = 0

    def __init__(self, course_name, course_instructor, course_date, course_time, course_duration, course_location, course_status, course_description):
        super().__init__(course_name, course_instructor, course_date, course_time, course_duration, course_status, course_description)
        Offline.count_id += 1
        self.__course_id = Offline.count_id
        self.__course_location = course_location

    def get_course_id(self):
        return self.__course_id

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def get_course_location(self):
        return self.__course_location

    def set_course_location(self, course_location):
        self.__course_location = course_location
