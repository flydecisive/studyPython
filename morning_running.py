x = int(input())
y = int(input())
days = 1

while x < y:
    x = x + x * 0.1
    days = days + 1
print(days)
