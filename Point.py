import Voucher

class Point(Voucher.Voucher):
    count_id = 0
    def __init__(self,product_name,claimed,expiry ,status,code, points_needed ):
        super().__init__(product_name, claimed, expiry,status, code)
        Point.count_id += 1
        self.__point_id = Point.count_id
        self.__points_needed = points_needed


    def get_point_id(self):
        return self.__point_id

    def get_points_needed(self):
        return self.__points_needed


    def set_point_id(self,point_id):
        self.__point_id = point_id

    def set_points_needed(self, points_needed):
        self.__points_needed = points_needed


