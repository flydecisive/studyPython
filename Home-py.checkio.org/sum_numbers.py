def sum_numbers(text):
    '''Функция возвращает сумму чисел в строке, 
        если число не является частью слова'''
    words = text.split(' ')
    numbers = []
    sum = 0
    for word in words:
        if word == '':
            break
        elif not word.isalpha():
            count = 0
            for letter in word:
                if letter.isalpha():
                    count += 1
            if count > 0:
                continue
            else:
                numbers.append(int(word))

    for number in numbers:
        sum += number

    return sum
    

print(sum_numbers(''))