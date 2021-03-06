﻿"""
Дан список из N (N≤2*10⁵) элементов, которые
принимают целые значения от 0 до 100.
Отсортируйте этот список в порядке неубывания
элементов. Выведите полученный список.
Решение оформите в виде функции CountSort(A),
которая модифицирует передаваемый ей список.
Использовать встроенные функции сортировки нельзя.
"""


grades = [0] * (2 * 10 ** 5)
A = map(int, input().split())


def countSort(A):
    for now in A:
        grades[now] += 1
    for grade in range(len(grades)):
        print((str(grade) + ' ') * grades[grade], end='')


countSort(A)
