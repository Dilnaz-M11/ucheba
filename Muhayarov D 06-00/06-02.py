n = int(input("Введите кол-во названных городов: "))
a = set()
b = 0
c = 0
d = 0
while c == 0:
    if b == n:
        d = input("Последний город: ")
        break
    else:
        f = input("Город: ")
    b = b + 1
    a.add(f)
if d not in a:
    print('OK')
else:
    print('TRY ANOTHER')