n = int(input("Введите кол-во записанных частей: "))
words = list()
for i in range(n):
    word = input("Введите строки: ")
    words.append(word)

txt = int(input("Введите сколько сделать объявлений: "))
for _ in range(txt):
    number = int(input("Введите номер объявления: "))
    print(words[number - 1])