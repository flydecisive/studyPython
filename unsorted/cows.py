n = int(input())

if n % 10 == 0 or (5 < n and n <= 20) or (5 <= n % 10 and n % 10 <= 9):
    print(n, "korov")
elif n == 1 or n % 10 == 1:
    print(n, "korova")
elif (2 <= n and n < 5) or (2 <= n % 10 and n % 10 < 5):
    print(n, "korovy")
