"""
Найдите количество положительных
элементов в данном списке.
"""

k = 0
numList = list(map(int, input().split()))
for i in range(0, len(numList)):
    if numList[i] > 0:
        k += 1
print(k, end=' ')
