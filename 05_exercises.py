"""
1. WHICH PIZZA HAS THE BEST PRICE/QUANTITY RATIO?

Write a program(or function) that will compare the area/price ratio between two
pizzas.
"""

from math import pi

radius1 = 32
radius2 = 36
price1 = 15
price2 = 20

def circle_area_to_price(radius, price):

	area = pi * radius ** 2
	return area / price2

ratio = circle_area_to_price(radius1, price1)
print(f"For radius = {radius1} w. price {price1} \
	the ratio is {ratio:.2f}")
ratio = circle_area_to_price(radius2, price2)
print(f"For radius = {radius2} w. price {price2} \
	the ratio is {ratio:.2f}")