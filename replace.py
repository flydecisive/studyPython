#step 10-2

with open('learnin_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip().replace('Python', 'C'))