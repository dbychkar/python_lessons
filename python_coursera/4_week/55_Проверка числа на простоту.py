"""
Дано натуральное число n>1.
Проверьте, является ли оно простым.
рограмма должна вывести слово YES,
если число простое и NO, если
число составное. Решение оформите
в виде функции IsPrime(n), которая
возвращает True для простых чисел и
False для составных чисел. Количество
действий в программе должно быть
пропорционально квадратному корню из n.
"""


def isPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


n = int(input())
if isPrime(n):
    print('YES')
else:
    print('NO')
