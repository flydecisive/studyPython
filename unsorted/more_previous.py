n = int(input())
count = 0
t_value = n

while n != 0:
    n = int(input())
    if n > t_value:
        count += 1
    t_value = n
print(count)
