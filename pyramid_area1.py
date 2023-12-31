# each layer adds +2 prisms, ex: 1, 3, 5, 7 (odd)
# area of a square: A = s^2
# area of an equilateral triangle: A = s^2 * sqrt(3)/4

from math import *


def area(side, x):
    total = 0
    for i in range(1, x + 1):
        tri_area = (side*i) ** 2 * sqrt(3) / 4
        bottom = (side*(i-1)) ** 2 * sqrt(3) / 4
        sides_per = ((side ** 2) * i) * 3
        if i > 1:
            total += (tri_area + sides_per) - bottom
        else:
            total += (tri_area + sides_per)
    return total


side_len = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))

print(f'You need {area(side_len, layers):.2f} m^2 of gold foil to cover the pyramid')
