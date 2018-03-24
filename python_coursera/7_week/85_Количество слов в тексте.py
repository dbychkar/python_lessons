"""
Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку
sys) записан текст. Словом считается последовательность непробельных символов
идущих подряд, слова разделены одним или большим числом пробелов или символами
конца строки. Определите, сколько различных слов содержится в этом тексте.
"""


finput = open('input.txt', 'r', encoding='utf-8')
textline = finput.read()
text = list(textline.split())
words = set()

for i in text:
    words.add(i)

print(len(words))
