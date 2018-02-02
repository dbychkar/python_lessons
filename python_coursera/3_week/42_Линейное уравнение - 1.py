# Даны вещественные числа a, b, c, d, e, f.
# Известно, что система линейных уравнений:
# ax + by = e
# cx + dy = f
# имеет ровно одно решение.
# Выведите два числа x и y, являющиеся решением этой системы.
# Формат ввода
# Вводятся шесть чисел a, b, c, d, e, f
# - коэффициенты уравнений системы.
# Формат вывода
# Выведите ответ на задачу.
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
x = ((e * d) - (b * f)) / ((a * d) - (b * c))
y = ((a * f) - (e * c)) / ((a * d) - (b * c))
if x % 1 == 0:
    xSol = int(x)
else:
    xSol = x
if y % 1 == 0:
    ySol = int(y)
else:
    ySol = y
print(xSol, ySol)
