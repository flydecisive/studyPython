hours1 = int(input())
minutes1 = int(input())
seconds1 = int(input())
hours2 = int(input())
minutes2 = int(input())
seconds2 = int(input())
total_seconds1 = hours1 * 3600 + minutes1 * 60 + seconds1
total_seconds2 = hours2 * 3600 + minutes2 * 60 + seconds2
time_difference = total_seconds2 - total_seconds1
print(time_difference)
