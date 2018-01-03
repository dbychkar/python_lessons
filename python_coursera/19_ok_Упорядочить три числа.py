a = int(input())
b = int(input())
c = int(input())
if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    (c, b) = (b, c)
    print(a, b, c)
elif b <= a <= c:
    (b, a) = (a, b)
    print(a, b, c)
elif b <= c <= a:
    (b, a) = (a, b)
    (c, b) = (b, c)
    print(a, b, c)
elif c <= b <= a:
    (c, a) = (a, c)
    print(a, b, c)
elif c <= a <= b:
    a, c = c, a
    (c, b) = (b, c)
    print(a, b, c)
