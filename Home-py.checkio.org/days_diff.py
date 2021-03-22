import datetime
def days_diff(a, b):
    first_date = datetime.date(a[0], a[1], a[2])
    second_date = datetime.date(b[0], b[1], b[2])
    difference = abs(first_date - second_date)
    return difference.days

print(days_diff((1982, 4, 19), (1982, 4, 22)))