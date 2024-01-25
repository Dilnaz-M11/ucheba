number = float(input("Введите дробное число: "))

# Используем условие для определения знака числа
if number > 0:
    print("+")
elif number < 0:
    print("-")
else:
    print("0")