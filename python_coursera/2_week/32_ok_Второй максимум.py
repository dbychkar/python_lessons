num1 = int(input())
n = num1
num2 = int(input())
m = num2
if n < m:
    n, m = m, n
while num2 != 0:
    num2 = int(input())
    if n < num2:
        m = n
        n = num2
    elif m < num2 <= n:
        m = num2
print(m)
