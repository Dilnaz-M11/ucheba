number = float(input("Введите число: "))

# Проверяем, является ли число нулём или меньше по абсолютной величине одной миллионной
if abs(number) < 0.000001:
    # Выводим "миллион"
    print("миллион")
else:
    # Вычисляем обратное значение числа
    inverse_number = 1 / number
    # Выводим обратное значение числа
    print("Обратное число:", inverse_number)