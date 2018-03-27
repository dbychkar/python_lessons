"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то, которое меньше в лексикографическом
порядке.
Формат ввода
Вводится текст.
Формат вывода
Выведите ответ на задачу.
"""


finput = open('input.txt', 'r', encoding='utf-8')

text = list(finput.read().split())
words = {}
wordMax = -1
result = []

for key in text:
    words[key] = words.get(key, 0) + 1

    if words[key] > wordMax:
        wordMax = words[key]

for key in words:
    if words[key] == wordMax:
        result.append(key)

result.sort()
print(result[0])
