import math
a = float(input())
b = float(input())
c = float(input())
d = (b ** 2) - (4 * a * c)
if d == 0:
    x = -b / (2 * a)
    if x % 1 == 0:
        x1an = int(x)
    else:
        x1an = x
    print(x1an)
elif d < 0:
    y = math.sqrt(0 - d)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if x1 % 1 == 0:
        x1an = int(x1)
    else:
        x1an = x1
    if x2 % 1 == 0:
        x2an = int(x2)
    else:
        x2an = x2
    if x1an <= x2an:
        print('{} {}'.format(round(x1an, 6), round(x2an, 6)))
    else:
        print('{} {}'.format(round(x2an, 6), round(x1an, 6)))
