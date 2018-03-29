"""
Добавьте в предыдущий класс следующие методы:
__add__ принимающий вторую матрицу того же размера и
возвращающий сумму матриц
__mul__ принимающий число типа int или float и возвращающий матрицу,
умноженную на скаляр
__rmul__ делающий то же самое, что и __mul__.
Этот метод будет вызван в том случае, если аргумент находится справа.
Можно написать __rmul__ = __mul__
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

    def __mul__(self, other):
        result = []
        for i in self.inList:
            result.append(map(lambda x: x*other, i))
        return Matrix(result)

    def __rmul__(self, other):
        return self * other

    def __add__(self, other):
        result = []
        for i in range(len(self.inList)):
            result.append(list(map(lambda x, y: x + y,
                                   self.inList[i],
                                   other.inList[i]
                                   )
                               )
                          )
        return Matrix(result)


exec(stdin.read())
