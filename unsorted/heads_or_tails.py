'''Программа подбрасывает монетку 100 раз
 и считает сколько было орлов и сколько решек'''
import random

count = 0
head = 0
tail = 0

while count < 100:
    coin = random.randrange(2) 
    if coin == 0:
        tail += 1
    elif coin == 1:
        head += 1
    
    count += 1

print('Орлы: ' + str(head))
print('Решки: ' + str(tail))