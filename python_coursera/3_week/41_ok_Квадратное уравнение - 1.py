import math
a = float(input())
b = float(input())
c = float(input())
d = (b * b) - (4 * a * c)
if d == 0:
    root = -b / (2 * a)
    if root % 1 == 0:
        root1an = int(root)
    else:
        root1an = root
    print(root1an)
elif d < 0:
    puppy = math.sqrt(0 - d)
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    if root1 % 1 == 0:
        root1an = int(root1)
    else:
        root1an = root1
    if root2 % 1 == 0:
        root2an = int(root2)
    else:
        root2an = root2
    if root1an <= root2an:
        print('{} {}'.format(round(root1an, 6), round(root2an, 6)))
    else:
        print('{} {}'.format(round(root2an, 6), round(root1an, 6)))
