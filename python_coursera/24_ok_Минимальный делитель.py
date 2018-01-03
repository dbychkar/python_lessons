n = int(input())
i = 2
while i <= n and n % i != 0:
    i = i + 1
else:
    print(i)
