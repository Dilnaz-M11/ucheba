n = int(input("Введите кол-во запросов белого списка: "))
white_list = []
black_list = []
list = []
for i in range(n):
    word = input("Введите запросы белого списка: ")
    white_list.append(word)
n1 = int(input())
for _ in range(n1):
    word1 = input("Введите запросы на анализ: ")
    if word1 in white_list:
        list.append(word1)
    else:
        black_list.append(word1)
for c in range(len(list)):
    print(list[c])