def larger_root(p, q):
    d = discriminant(1, p, q)
    return (-p + d ** 0.5) / 2


def smaller_root(p, q):
    d = discriminant(1, p, q)
    return (-p - d ** 0.5) / 2


def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)


def main():
    p = float(input("Введите значение p: "))
    q = float(input("Введите значение q: "))
    print("Дискриминант: ", discriminant(1, p, q))
    print("Меньший корень: ", smaller_root(p, q), "Больший корень: ", larger_root(p, q))


main()