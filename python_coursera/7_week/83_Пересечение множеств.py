"""
Даны два списка чисел, которые могут содержать
до 10000 чисел каждый. Выведите все числа,
которые входят как в первый, так и во второй
список в порядке возрастания.
Примечание. И даже эту задачу на Питоне
можно решить в одну строчку.
"""


print(*sorted(set(input().split()) & set(input().split()), key=int))
