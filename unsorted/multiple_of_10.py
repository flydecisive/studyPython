#step 7-3
number = int(input('Напишите число, и я сообщу, кратно ли оно 10: '))
if number % 10 == 0:
    print('Число ' + str(number) + ' кратно 10')
else:
    print('Число ' + str(number) + ' не кратно 10')