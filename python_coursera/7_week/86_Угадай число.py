"""
Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
Беатриса пытается угадать это число, для этого она называет некоторые
множества натуральных чисел. Август отвечает Беатрисе YES, если среди
названных ей чисел есть задуманное или NO в противном случае.
После нескольких заданных вопросов Беатриса запуталась в том, какие
вопросы она задавала и какие ответы получила и просит вас помочь ей
определить, какие числа мог задумать Август.
    Формат ввода
Первая строка входных данных содержит число n — наибольшее число, которое
мог загадать Август. Далее идут строки, содержащие вопросы Беатрисы.
Каждая строка представляет собой набор чисел, разделенных пробелами.
После каждой строки с вопросом идет ответ Августа: YES или NO.
Наконец, последняя строка входных данных содержит одно слово HELP.
    Формат вывода
Вы должны вывести (через пробел, в порядке возрастания) все числа,
которые мог задумать Август.
"""
N = int(input())

fullArray = set()
for i in range(1, N+1):
    fullArray.add(i)

yesArray = set()
noArray = set()
tmpArray = set()

line = list(input().split())

while line[0] != 'HELP':
    answer = input()

    if answer == 'YES':
        for i in line:
            tmpArray.add(int(i))

        if len(yesArray) > 0:
            yesArray = yesArray & tmpArray
        else:
            yesArray = tmpArray
        tmpArray = set()
    else:
        for i in line:
            noArray.add(int(i))

    line = list(input().split())

# print(yesArray)
# print(noArray)
if len(yesArray) > 0:
    fullArray = fullArray & yesArray
print(*sorted(list(fullArray - noArray)))
