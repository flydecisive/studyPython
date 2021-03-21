def sum_numbers(text):
    '''Функция возвращает сумму чисел в строке, 
        если число не является частью слова'''
    words = text.split(' ')
    print(words)

sum_numbers('who is first here')