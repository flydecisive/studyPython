'''Игра загадывает слово из списка и говорит сколько букв в слове.
Дается 5 попыток, чтобы узнать, есть ли буква в слове
после этого игрок попробывать отгадать слово должен отгадать слово
'''
import random

WORDS = ('привет', 'жопа', 'чай', 'винегрет', 'омлет', 'судья', 'венок')

word = random.choice(WORDS)
length  = len(word)

greeting = '\t\tДобро пожаловать в игру угадай слово!\n'
greeting += '\tКомпьютер загадывает случайное слово, '
greeting += 'а вы должны его отгадать.\n\n'

rules = 'Правила:\n'
rules += '-Компьютер сообщает длину слова\n'
rules += '-У вас есть 5 попыток, чтобы отгадать есть ли буква в слове\n'
rules += '-После этоого у вас есть одна попытка, чтобы отгадать слово'

print(greeting, rules)
print('Удачи!')

print('-------------------------------------\n')
print('Длина слова: ' + str(length) + ' букв')
count = 0
while count < 5:
    attempt = input('Попробуйте угадать букву в слове: ')
    if attempt in word:
        print('Да')
    else:
        print('Нет')
    count += 1

guess = input('\nПора угадывать слово! Ваш ответ: ')
if guess == word:
    print('Поздравляю, вы угадали!')
else:
    print('К сожалению это не правильный ответ!')
    print('Загаданное слово - ' + word)
