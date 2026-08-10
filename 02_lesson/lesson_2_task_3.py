import math


def square(side):
    area = side * side
    return math.ceil(area)


side = 4.5
result = square(side)
print(f"Площадь квадрата со стороной {side} : {result}")
