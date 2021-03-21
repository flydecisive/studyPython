def split_pairs(a):
    '''Функция возвращает список из пар символов исходной строки'''
    list_of_pairs = []
    count = 0
    ind = 0
    pair = ''
    while count <= len(a) - 1:
        pair += a[ind]
        ind += 1
        count += 1
        if len(pair) == 2:
            list_of_pairs.append(pair)
            pair = ''
    if len(a) % 2 != 0:
        pair = ''
        pair += a[-1] + '_'
        list_of_pairs.append(pair)
    
    return list_of_pairs

print(split_pairs('abcdf'))