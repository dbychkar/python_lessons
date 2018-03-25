"""
Каждый из N школьников некоторой школы знает Mᵢ языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы
один из школьников.
    Формат ввода
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mᵢ, после каждого из чисел идет Mᵢ строк, содержащих
названия языков, которые знает i-й школьник.
Длина названий языков не превышает 1000 символов, количество различных
языков не более 1000. 1≤N≤1000, 1≤Mᵢ≤500.
    Формат вывода
В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков. Затем - количество языков,
которые знает хотя бы один школьник, на следующих строках - список таких
языков.
"""


finput = open('input.txt', 'r', encoding='utf-8')
N = int(finput.readline())

tmp = set()
lang = []
langs = []
allKnow = set()
oneKnow = set()

for i in range(1, N+1):
    K = int(finput.readline())
    for j in range(1, K+1):
        lang = list(finput.readline().split())
        tmp.add(lang[0])

    langs.append(tmp)
    tmp = set()

allKnow = langs[0]
oneKnow = langs[0]

for i in langs:
    allKnow = allKnow & i
    oneKnow = oneKnow | i

print(len(allKnow))
if len(allKnow) > 0:
    print(*allKnow, sep='\n')
print(len(oneKnow))
print(*oneKnow, sep='\n')
