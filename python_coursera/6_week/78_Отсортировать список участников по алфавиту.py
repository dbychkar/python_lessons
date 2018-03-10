"""
Известно, что фамилии всех участников — различны.
Сохраните в массивах список всех участников и
выведите его, отсортировав по фамилии в лексикографическом
порядке. При выводе указываете фамилию, имя участника и его балл.

Используйте для ввода и вывода файлы input.txt и output.txt
с указанием кодировки utf8. Например, для чтения откройте
файл с помощью open('input.txt', 'r', encoding='utf8')
"""

finput = open('input.txt', 'r', encoding='utf-8')
foutput = open('output.txt', 'w', encoding='utf-8')

members = []

for i in finput:
    line = i.split()
    members.append(line[0] + ' ' + line[1] + ' ' + line[3])

members.sort()
for i in members:
    print(i, file=foutput)
foutput.close()
