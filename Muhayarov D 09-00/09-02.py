n = int(input("Введите кол-во строк: "))
list = []
for i in range(n):
    word = input("Введите запросы: ")
    list.append(word)
word1 = input("Введите свой запрос: ")
for i in list:
    if word1 in i:
        print(i)