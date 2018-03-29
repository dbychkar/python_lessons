"""
Добавьте в программу из предыдущей задачи класс MatrixError,
содержащий внутри self поля matrix1 и matrix2 (ссылки на матрицы)
В класс Matrix внесите следующие изменения:
- Добавьте в метод __add__ проверку на ошибки в размере входных данных,
чтобы при попытке сложить матрицы разных размеров было выброшено исключение
MatrixError таким образом, чтобы matrix1 поле MatrixError стало первым
аргументом __add__ (просто self),
а matrix2 — вторым (второй операнд для сложения).
- Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат
(данный метод модифицирует экземпляр класса Matrix)
- Реализуйте статический метод transposed, принимающий Matrix и возвращающий
транспонированную матрицу.
"""
import copy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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
        if self.size() != other.size():
            raise MatrixError(self, other)
        result = []
        for i in range(len(self.inList)):
            result.append(list(map(lambda x, y: x + y,
                                   self.inList[i],
                                   other.inList[i]
                                   )
                               )
                          )
        return Matrix(result)

    def transpose(self):
        n = len(self.inList)
        m = len(self.inList[0])

        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(self.inList[j][i])
            self.inList.append(temp)

        for i in range(n):
            del self.inList[0]

        return self

    @staticmethod
    def transposed(object):
        newMatrix = Matrix(copy.deepcopy(object.inList))
        return newMatrix.transpose()


exec(stdin.read())
