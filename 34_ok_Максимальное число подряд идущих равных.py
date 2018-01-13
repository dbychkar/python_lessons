n = int(input())
m = n
i = k = 1
while n:
    n = int(input())
    if n == m:
        i += 1
    elif m != n:
        m = n
        i = 1
    if k < i:
        k = i
print(k)
