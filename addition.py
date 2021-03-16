#step 10-6 and step 10-7
while True:
    number = input('Введите первое число или "q" для выхода: ')
    if number == 'q':
        break
    number2 = input('Введите второе число или "q" для выхода: ')
    if number2 == 'q':
        break
    
    try:
        number = int(number)
        number2 = int(number2)
    except ValueError:
        print('Вы ввели не число!')
    else:
        sum = number + number2
        print(str(number) + ' + ' + str(number2) + ' = ' + str(sum))