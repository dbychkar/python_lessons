﻿"""
Отсортируйте данный массив, используя встроенную сортировку.
Формат ввода
Первая строка входных данных содержит количество
элементов в массиве N, N ≤ 10⁵.
Далее идет N целых чисел, не превосходящих по
абсолютной величине 10⁹.
Формат вывода
Выведите эти числа в порядке неубывания
"""


myList = int(input())
myAnotherList = list(map(int, input().split()))
myAnotherList.sort()
print(' '.join(map(str, myAnotherList)))
