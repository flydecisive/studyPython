def beginning_zeros(number):
    '''Функция возвращает количество нулей в начале строки'''
    if number[0] != '0':
        answer = 0
    else:
        count = 0
        for num in number:
            if num == '0':
                count += 1
            else:
                break
        answer = count
    
    return answer

print(beginning_zeros('0000'))