x = int(input())
y = int(input())
i = 0
while y - x > 0:
    x = x + 0.1 * x
    i = i + 1
else:
    print(i + 1)
