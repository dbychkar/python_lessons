"""
В списке все элементы различны. Поменяйте местами
минимальный и максимальный элемент этого списка.

Формат ввода
Вводится список целых чисел. Все числа
списка находятся на одной строке.
"""


numList = list(map(int, input().split()))
tmp = 0
if (len(numList) != 0):
    Min = numList[0]
    Max = numList[0]

for i in range(0, len(numList)):
    if (Min >= numList[i]):
        Min = numList[i]
        IndexMin = i
    if (Max <= numList[i]):
        Max = numList[i]
        IndexMax = i
tmp = numList[IndexMin]
numList[IndexMin] = numList[IndexMax]
numList[IndexMax] = tmp
print(' '.join(map(str, numList)))
