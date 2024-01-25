n = int(input("Введите количество чисел: "))
m = int(input("Введите начало набора: "))
k = int(input("Введите конец набора: "))
num = list()
for i in range(n):
    number = int(input("Введите число для списка: "))
    num.append(number ** 2)
if m > 0 and m < len(num) and k > 0 and k < len(num):
    print(sum(num[m:k + 1]))