from math import *

def area(side, n):
    num_sides = ((n ** 2) + n) / 2 # think of this as factorial, but addition. amount of sides increase by one as you go down the prism
    total = ((side ** 2) * num_sides * 3) + ((side*n) ** 2 * sqrt(3) / 4)
    return total


side_len = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))

print(f'You need {area(side_len, layers):.2f} m^2 of gold foil to cover the pyramid')
