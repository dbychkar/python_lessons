n = int(input())
k = 0
i = 1
while i <= n:
    s = 1.0 / (i**2)
    k += s
    i = i + 1
print('{:,g}'.format(k))
