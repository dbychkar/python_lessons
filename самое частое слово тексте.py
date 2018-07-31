"""
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.
"""

# wordcount={}
# c = 0
# x = ''
# with open('dataset_3363_3.txt') as inf:
#     for line in inf:
#         line = line.strip()
#         for word in line.lower().split():
#             if word not in wordcount:
#                 wordcount[word] = 1
#             else:
#                 wordcount[word] += 1
# for k,v in sorted(wordcount.items()):
#     if v > c:
#         c = v
#         x = k
# print(x, c)



wordcount = {}
c = 0
x = ''
myStr = 'cdZYUTpdU YX TT TYTYa TT dadaaUTbU pZYUTU cTTdcXT TT ccZcpT pZYUTU aUd YZcdbZ bTbZ cdZYUTpdU TdcTcdXTp UXpT bbpbZXUT '.lower(
).split()
for i in myStr:
    if i not in wordcount:
        wordcount[i] = 1
    else:
        wordcount[i] += 1

print(wordcount)

for k, v in sorted(wordcount.items()):
    if v > c:
        c = v
        x = k
print(x, c)
