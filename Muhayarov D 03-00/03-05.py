initial_coins = int(input())

# Пока количество монет делится на 8, делим его на 8 и уменьшаем исходное количество монет на 7/8
while initial_coins % 8 == 0:
    initial_coins = initial_coins // 8

# Выводим первую цифру оставшегося количества монет
print(str(initial_coins)[0])