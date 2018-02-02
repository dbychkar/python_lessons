x = int(input())
y = int(input())
xn = x
i = 0
while xn <= y:
    xn = xn + 0.1 * xn
    i = i + 1
else:
    print(i + 1)
