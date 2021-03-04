#step 4-8
coubs = []
for coub in range(1, 11):
    coubs.append(coub**3)
for coub in coubs:
    print(coub)

print("\nlist comprehension\n")


#step 4-9
list_coubs = [coub**3 for coub in range(1, 11)]
for coub in coubs:
    print(coub)