def checkio(array):
    '''Функция суммирует все элементы с четными индексами и умножает на
    последний элемент исходного массива'''
    sum = 0
    count = 0
    if len(array) == 0:
        multiple = 0
    else:
        while count <= len(array) - 1:
            sum += array[count]
            count += 2
        multiple = sum * array[-1]

    return multiple

print(checkio([]))