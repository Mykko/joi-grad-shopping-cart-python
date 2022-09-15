# -*- coding: utf-8 -*-
# @Author: mykko
# @Date:   2022/9/14 21:23
from enum import Enum


def dis_(products):
    need_products = {"DIS_10_PRODUCT1", "DIS_10_PRODUCT2", "DIS_10_PRODUCT3"}

    for product in products:
        if product not in need_products:
            continue
        if product.product_code.startswith("DIS_10"):
            product.dis_count_price *= 0.9
            product.loyalty_points_earned = product.price // 10
        elif product.product_code.startswith("DIS_15"):
            product.dis_count_price *= 0.85
            product.loyalty_points_earned = product.price // 15
        elif product.product_code.startswith("DIS_20"):
            product.dis_count_price *= 0.8
            product.loyalty_points_earned = product.price // 20
        else:
            product.loyalty_points_earned = product.price // 5


def three_for_two(products):
    need_products = {"DIS_10_PRODUCT1", "DIS_10_PRODUCT2", "DIS_10_PRODUCT3"}
    product_count = {}
    for product in products:
        if product not in need_products:
            continue
        if product.product_code not in product_count:
            product_count[product.product_code] = 0
        product_count[product.product_code] += 1
        if product_count[product.product_code] % 3 == 0:
            product.dis_count_price = 0
            product.loyalty_points_earned = 0


def five_hundreds_dis_five(products):
    need_products = {"DIS_10_PRODUCT1", "DIS_10_PRODUCT2", "DIS_10_PRODUCT3"}
    total_price = 0
    for product in products:
        if product not in need_products:
            continue
        total_price += product.dis_count_price
    if total_price >= 500:
        for product in products:
            if product not in need_products:
                continue
            product.dis_count_price *= 0.95


def loyalty_points_earned(products):
    return


class Discount(Enum):
    dis_ = 1
    three_for_two = 2
    five_hundreds_dis_five = 3
    loyalty_points_earned = 4


discount_dict = {Discount.dis_: dis_,
                 Discount.five_hundreds_dis_five: five_hundreds_dis_five,
                 Discount.three_for_two:three_for_two,
                 Discount.loyalty_points_earned:loyalty_points_earned
                 }


if __name__ == '__main__':
    print(discount_dict[Discount.dis_])


