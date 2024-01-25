borya = int(input())
vova = int(input())
dima = int(input())

# создаем список с ростом мальчиков
boys = [borya, vova, dima]

# сортируем список по убыванию
boys.sort(reverse=True)

# выводим рост мальчиков по убыванию
for height in boys:
    print(height)