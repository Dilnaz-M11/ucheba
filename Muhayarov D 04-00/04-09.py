n = int(input('Введите высоту : '))
for i in range(1, n + 1, 1):
    print(' ' * (n - i), '*' * (2 * i - 1))