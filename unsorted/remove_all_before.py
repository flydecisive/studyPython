def remove_all_before(items, border):
    '''Функция удаляет все элементы до нужного элемента'''
    if len(items) == 0:
        answer = items
    elif border not in items:
        answer = items
    else:
        count = 0
        while count != len(items):
            if items[count] != border:
                items.pop(count)
            elif items[count] == border:
                break
        answer = items
    
    return answer

print(remove_all_before([1, 2, 3, 4, 5], 3))