num = int(input())
count = 2

while count > 0:
    if num % count == 0:
        print(count)
        break
    else:
        count = count + 1
