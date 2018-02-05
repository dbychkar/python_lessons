def min4(a, b, c, d):
    min1 = min(a, b)
    min2 = min(c, d)
    min3 = min(min1, min2)
    return min3
a1 = int(input())
b1 = int(input())
c1 = int(input())
d1 = int(input())
print(min4(a1, b1, c1, d1))
