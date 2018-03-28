"""
Булева функция XOR (сложение по модулю два) задаётся следующей таблицей истинности:
xor(0,0)=0
xor(0,1)=1
xor(1,0)=1
xor(1,1)=0
На вход подаются две последовательности (a₁,…,an) и (b₁,…,bn) из 0 и 1.
Вычислите последовательность из (c₁,…,cn), где каждая cᵢ=xor(aᵢ,bᵢ).
Формат ввода
На вход подаются две строки из 0 и 1, разделённых пробелами.
Первая строка — это последовательность (a₁,…,an).
Вторая строка — это последовательность (b₁,…,bn).
Формат вывода
Выведите последовательность (c₁,…,cn), разделяя каждый элемент пробелом
Примечания
Для решения задачи можете использовать функцию zip.
"""


print(
    *list(
        map(
            lambda x: x[0] ^ x[1],
            zip(
                map(
                    int,
                    input().split()
                ),
                map(
                    int,
                    input().split()
                )
            )
        )
    )
)
