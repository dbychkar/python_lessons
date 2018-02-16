"""
Дан список чисел. Выведите все
элементы списка, которые больше
предыдущего элемента.
"""


L = list(map(int, input().split()))
for i in range(1, len(L)):
    if L[i] > L[i - 1]:
        print(L[i], end=' ')
