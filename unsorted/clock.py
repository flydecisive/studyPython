n = int(input())
hours = n // 60 // 60 % 24
minutes1 = n // 60 % 60 % 10
minutes2 = n // 60 % 60 // 10
minutes = str(minutes2) + str(minutes1)
seconds1 = n % 60 % 10
seconds2 = n % 60 // 10
seconds = str(seconds2) + str(seconds1)
print(hours, minutes, seconds, sep=":")