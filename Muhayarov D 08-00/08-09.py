for i in range(int(input("Введите кол-во строк подлежащих обработке: "))):
    word = input("Введите строчку: ")
    if '%' in word:
        print(word.replace('%', ''))
    elif '#' in word:
        print("")
    else:
        print(word)