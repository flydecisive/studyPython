def nearest_value(values, one):
    '''Функция возвращает ближайшее целое число к переданному числу'''
    numbers = sorted(list(values))
    if one not in values and one >= numbers[-1]:
        answer = numbers[-1]
    elif one not in values:
        values.add(one)
        numbers = sorted(list(values))
        count = 0
        while count <= len(numbers):
            if numbers[count] == one:
                first = numbers[count - 1]
                second = numbers[count + 1]
                break
            count += 1

        if abs(one - first) < abs(second - one):
            answer = first
        elif abs(one - first) == abs(second - one):
            if first < second:
                answer = first
            else:
                answer = second
        else:
            answer = second
    else:
        answer = one

    return answer

print(nearest_value({4, 7, 10, 11, 12, 17}, 0))