'''Программа выводит слова из списка в случайном порядке'''
import random

words = ['Привет', 'Hello', 'Честь', 'Лига', 'Компьютер']
print('Исходный список слов: ', end='')
print(words, '\n')

print('Слова в рандомном порядке: ')
while words:
    choice = random.choice(words)
    print(choice)
    words.remove(choice)
