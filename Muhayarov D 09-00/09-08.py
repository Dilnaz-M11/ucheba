n = int(input("Введите кол-во дней: "))
list = ["щи", "борщ", "щавеливый суп", "овсяный суп", "суп по-чабански",]
for i in range(n):
    print(list[i % len(list)])