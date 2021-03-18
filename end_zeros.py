def end_zeros(num):
    '''Функция считает количество нулей в конце числа'''
    num = str(num)
    count = -1
    if len(num) == 1:
        if num == '0':
            count = 1
        else:
            count = 0
    else:
        while True:
            if num[count] == '0':
                count -= 1
            else:
                count = -count - 1
                break
    return count

print(end_zeros(0))