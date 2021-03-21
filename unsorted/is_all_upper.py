def is_all_upper(text):
    '''Фунцкция проверяет, являются ли все буквы в строке заглавными'''
    count = 0
    answer = False
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if len(text) == 0:
        answer = True
    else:
        for letter in text:
            if letter.isalpha():
                if letter == letter.upper():
                    count += 1
            elif letter == ' ':
                count += 1
            elif letter in numbers or letter == ' ':
                count += 1
    
    if len(text) == count:
        answer = True
        
    return answer

print(is_all_upper('  '))