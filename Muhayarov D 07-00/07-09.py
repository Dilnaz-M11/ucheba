message = input("Введите сообщение: ")
number = int(input("Введите номер: "))

if number < 1 or number > len(message):
    print("Ошибка")
else:
    letter = message[number-1]
    print(letter)