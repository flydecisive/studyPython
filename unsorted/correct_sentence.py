def correct_sentence(text):
    '''Возвращает исправленный текст с начальной большой буквой и 
        точкой в конце'''
    new_text = text[0].capitalize() + text[1:]
    if text[-1] != '.':
        new_text += '.'

    return new_text

print(correct_sentence('Greetings, friends.'))