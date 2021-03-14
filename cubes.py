#step 9-14
from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides)
        print(roll)

six_sides = Die()
print('Броски 6 гранного кубика: ')
count = 1
while count <= 10:
    six_sides.roll_die()
    count += 1

ten_sides = Die(10)
print('\nБроски 10 гранного кубика: ')
count = 1
while count <= 10:
    ten_sides.roll_die()
    count += 1

twenty_sides = Die(20)
print('\nБроски 20 гранного кубика: ')
count = 1
while count <= 10:
    twenty_sides.roll_die()
    count += 1
