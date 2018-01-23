a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
s = float(p * (p - a) * (p - b) * (p - c)) ** 0.5
print('{:,g}'.format(s))
