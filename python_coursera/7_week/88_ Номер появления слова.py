"""
Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных подряд идущих символов.
Слова разделены одним или большим числом пробелов или символами конца строки.
Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось
в этом тексте ранее.
Формат ввода
Вводится текст.
Формат вывода
Выведите ответ на задачу.
"""
finput = open('input.txt', 'r', encoding='utf-8')
text = list(finput.read().split())
words = {}
result = []

for key in text:
    if key in words:
        result.append(words[key])
    else:
        result.append(0)
    words[key] = words.get(key, 0) + 1
print(*result)
