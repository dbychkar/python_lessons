from math import floor
p = int(input())
x = int(input())
y = int(input())
sum = ((x * 100 + y) * (p / 100)) + (x * 100 + y)
print(int((sum // 100)), floor(sum % 100))
