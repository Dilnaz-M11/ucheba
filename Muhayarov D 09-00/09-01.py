n = int(input("Сколько покупок: "))
list = []
for i in range(n):
    word = input("Напишите товар: ")
    list.append(word)
for word in list:
    print(word)