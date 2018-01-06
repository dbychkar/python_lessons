now = int(input())
nowMax = now
while now != 0:
    if now > nowMax:
        nowMax = now
    now = int(input())
print(nowMax)
