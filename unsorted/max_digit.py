def max_digit(number):
    '''Функция возвращает максимальную цифру в числе'''
    digits = str(number)
    max = int(digits[0])
    for digit in digits:
        if int(digit) > max:
            max = int(digit)

    return max

print(max_digit(1000))