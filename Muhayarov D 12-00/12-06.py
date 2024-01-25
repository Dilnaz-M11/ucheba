n = input("Введите строку: ")
print(' '.join('-'.join(i) for i in n.upper().split(' ')))