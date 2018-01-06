n = int(input())
if n % 10 == 1 and n != 11:
    print(n, 'korova')
elif 2 <= n % 10 <= 4 and n // 10 != 1:
    print(n, 'korovy')
else:
    print(n, 'korov')
