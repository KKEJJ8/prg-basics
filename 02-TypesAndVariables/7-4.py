# A program that checks whether a tree can be cut down based on its circumference.
# A tree may be cut down if its diameter is at least 50 cm.

import math

circumference = float(input('Enter tree circumference in cm: '))


diameter = circumference / math.pi


can_cut_down = diameter >= 50


print(f'Tree can be cut down: {can_cut_down}')