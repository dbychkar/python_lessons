a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
if a1 == c2 and b1 == b2 and c1 == a2 or a1 == c2 and b1 == a2 and c1 == b2:
    print('Boxes are equal')
elif a1 == a2 and b1 == b2 and c1 == c2 or a1 == a2 and b1 == c2 and c1 == b2:
    print("Boxes are equal")
elif a1 == b2 and b1 == c2 and c1 == a2 or a1 == b2 and b1 == a2 and c1 == c2:
    print("Boxes are equal")
elif a1 >= a2 and b1 >= b2 and c1 >= c2 \
        or a1 >= a2 and b1 >= c2 and c1 >= b2 \
        or a1 >= b2 and b1 >= a2 and c1 >= c2 \
        or a1 >= b2 and b1 >= c2 and c1 >= a2:
    print("The first box is larger than the second one")
elif a1 >= c2 and b1 >= b2 and c1 >= a2 or a1 >= c2 and b1 >= a2 and c1 >= b2:
    print("The first box is larger than the second one")
elif a1 <= a2 and b1 <= b2 and c1 <= c2 \
        or a1 <= a2 and b1 <= c2 and c1 <= b2 \
        or a1 <= b2 and b1 <= a2 and c1 <= c2 \
        or a1 <= b2 and b1 <= c2 and c1 <= a2:
    print("The first box is smaller than the second one")
elif a1 <= c2 and b1 <= b2 and c1 <= a2 or a1 <= c2 and b1 <= a2 and c1 <= b2:
    print("The first box is smaller than the second one")
else:
    print('Boxes are incomparable')
