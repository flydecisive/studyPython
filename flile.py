#step 10-1

with open('pi_digits.txt') as file_object:
    file = file_object.read()

print(file)

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

print()

with open('pi_digits.txt') as file_object:
    file_list = file_object.readlines()
    for line in file_list:
        print(line.rstrip())