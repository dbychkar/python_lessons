"""
Даны два натуральных числа n и m.
Сократите дробь (n / m), то есть
выведите два других числа p и q
таких, что (n / m) = (p / q) и дробь
(p / q) — несократимая.
Решение оформите в виде функции
ReduceFraction(n, m), получающая
значения n и m и возвращающей
кортеж из двух чисел (return p, q).
"""


def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)


def ReduceFraction(n, m):
    x = gcd(n, m)
    p = n // x
    q = m // x
    return p, q

n = int(input())
m = int(input())
p, q = ReduceFraction(n, m)
print(p, q)
