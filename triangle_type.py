a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (c + b > a) and (a + c > b):
    if a ** 2 == b ** 2 + c ** 2:
        print("rectangular")
    elif b ** 2 == a ** 2 + c ** 2:
        print("rectangular")
    elif c ** 2 == a ** 2 + b ** 2:
        print("rectangular")
    elif a ** 2 > b ** 2 + c ** 2:
        print("obtuse")
    elif b ** 2 > a ** 2 + c ** 2:
        print("obtuse")
    elif c ** 2 > a ** 2 + b ** 2:
        print("obtuse")
    elif a ** 2 < b ** 2 + c ** 2:
        print("acute")
    elif b ** 2 < a ** 2 + c ** 2:
        print("acute")
    elif c ** 2 > a ** 2 + b ** 2:
        print("acute")
else:
    print("impossible")
