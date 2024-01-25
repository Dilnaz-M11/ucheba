n = int(input("Введите кол-во строк: "))
list = []
for i in range(n):
    word = input("Введите строки: ")
    list.append(word)
nature = int(input("Введите номер буквы: "))
for i in list:
    if nature > len(i):
        continue
    print(i[nature - 1], end="")