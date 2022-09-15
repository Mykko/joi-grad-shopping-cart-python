from src.model.Discount import Discount
class Product:
    def __init__(self, price, product_code, name):
        self.price = price
        self.product_code = product_code
        self.name = name

        self.dis_count_price = price
        self.loyalty_points_earned = price // 5


    def __str__(self):
        return " Name: %s \n Price: %s \n" % (self.name, self.price)
