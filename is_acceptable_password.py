def is_acceptable_password(password):
    '''Функция проверят длину пароля'''
    if len(password) <= 6:
        answer = False
    else:
        answer = True
    return answer