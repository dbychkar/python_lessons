"""
Во входной строке записана последовательность чисел
через пробел. Для каждого числа выведите слово YES
(в отдельной строке), если это число ранее встречалось
в последовательности или NO, если не встречалось.
"""


N = list(map(int, input().split()))
M = set()
for i in N:
    if i in M:
        print('YES')
    else:
        print('NO')
    M.add(i)
