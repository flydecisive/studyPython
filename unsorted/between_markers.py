def between_markers(text, begin, end):
    '''Возвращает подстроку между двумя данными маркерами'''
    count = 0
    for letter in text:
        count += 1
        if letter == begin:
            first_pos = count
        if letter == end:
            second_pos = count - 1

    return text[first_pos:second_pos]

print(between_markers('[apple]', '[', ']'))