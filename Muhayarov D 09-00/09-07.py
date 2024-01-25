n = int(input("Введите кол-во строк: "))
list = []
list1 = []
for i in range(n):
    word = input("Введите запросы: ")
    list.append(word)
n1 = int(input("Введите кол-во запросов: "))
for _ in range(n1):
    word1 = input()
    list1.append(word1)
for words in list:
    for words1 in list1:
        if words1 in words:
            print(words)
            break
