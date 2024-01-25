n = int(input("Введите кол-во строк: "))
c = 0
for i in range(n):
    text = input("Введите строки: ")
    c += 1
    if "кот" in text:
        print(c, text.find("кот") + 1)