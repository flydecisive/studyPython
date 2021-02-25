n = int(input())
max = 0
pre_max = 0

while n != 0:
    if n >= max:
        pre_max = max
        max = n
    elif n >= pre_max and n < max:
        pre_max = n
    n = int(input())

print(pre_max)
