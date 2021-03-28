numbers = []

while True:
    number = int(input())
    if number == 0:
        break
    else:
        numbers.append(number)

max = numbers[0]
for number in numbers:
    if number > max:
        max = number

count = 0
for number in numbers:
    if number == max:
        count += 1

print(count)
