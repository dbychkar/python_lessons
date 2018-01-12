n = int(input())
m = n
i = 1
while n:
    n = int(input())
    if n > m:
        m = n
        i = 1
    else:
        if m == n:
            i += 1
if i > 0:
    print(i)
else:
    print(0)
