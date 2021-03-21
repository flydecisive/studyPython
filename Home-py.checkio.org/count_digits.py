def count_digits(text):
    '''Функция возвращает количество цифр в строке'''
    words = text.split(' ')
    count = 0
    if len(text) == 0:
        count = 0
    else:
        for word in words:
            for letter in word:
                if letter.isdigit():
                    count += 1
    return count

print(count_digits(''))