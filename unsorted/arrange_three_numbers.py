a, b, c = int(input()), int(input()), int(input())

if a >= b and b >= c:
    print(c, b, a)
elif a >= c and c >= b:
    print(b, c, a)
elif b >= a and a >= c:
    print(c, a, b)
elif b >= c and c >= a:
    print(a, c, b)
elif c >= a and a >= b:
    print(b, a, c)
elif c >= b and b >= a:
    print(a, b, c)
