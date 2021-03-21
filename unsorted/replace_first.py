def replace_first(items):
    '''Функция переставляет первый элемент списка в конец'''
    if len(items) == 0 or len(items) == 1:
        answer = items
    else:
        popped = items.pop(0)
        items.append(popped)
        answer = items

    return answer

print(replace_first([1, 2, 3, 4]))