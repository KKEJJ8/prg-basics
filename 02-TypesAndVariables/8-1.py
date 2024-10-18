# Calculation of circle area and circumference 

import math


r = float(input('Enter the radius of the circle: '))
pi = math.pi  


area = pi * (r ** 2)


circumference = 2 * pi * r


print(f'For a circle with radius {r}:')
print(f'Circumference: {circumference:.2f}')
print(f'Area: {area:.2f}')