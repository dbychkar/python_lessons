"""
Реализуйте класс Matrix. Он должен содержать:
Конструктор от списка списков.
- Метод __str__ переводящий матрицу в строку.
- Метод size без аргументов, возвращающий кортеж вида
(число строк, число столбцов)
"""


from sys import stdin
import copy


class Matrix:
    def __init__(self, inList):
        self.inList = copy.deepcopy(inList)

    def __str__(self):
        text = []
        for i in self.inList:
            text.append('\t'.join(map(str, i)))
        return '\n'.join(text)

    def size(self):
        return len(self.inList), len(self.inList[0])


exec(stdin.read())
