text1 = str(input("Введите слово 1: "))
text2 = str(input("Введите слово 2: "))
while text1[-1] == text2[0]:
    text = str(input("Введите слово : "))

    if text[-1] == text2[0]:
        text2 = str(input("Введите новое слово : "))

    else:
        print(text)
        break