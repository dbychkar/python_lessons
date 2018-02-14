"""
Выведите все четные элементы списка.
"""


numList = list(map(int, input().split()))
for i in range(0, len(numList)):
    if numList[i] % 2 == 0:
        print(numList[i], end=' ')
