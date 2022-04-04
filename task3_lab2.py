# 15. Дано координати (x; y) точки і радіус кола (r). Визначити чи належить дана точка колі, якщо його
# центр знаходиться на початку координат.
import math


def circle(a, b, radius_ci):
    hyp = math.sqrt(math.pow(a, 2)+math.pow(a, 2))
    if hyp <= radius_ci:
        print("Дана точка належить колу")
    else:
        print("Дана точка не належить колу")


x = float(input("Введіть координату x: "))
y = float(input("Введіть координату y: "))
r = float(input("Введіть радіус кола: "))
circle(x, y, r)
