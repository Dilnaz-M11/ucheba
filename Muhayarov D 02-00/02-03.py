import math

# Длина рва
length_of_trench = 1400

# Длина, которую один землекоп может прокопать за день
length_per_day = 3

# Рассчитываем количество землекопов
num_of_workers = math.ceil(length_of_trench / length_per_day)

print(num_of_workers)