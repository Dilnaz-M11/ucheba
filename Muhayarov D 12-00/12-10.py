n = input("Введите строку: ")
c = 0
for word in n:
    if word != " " and n !="\t":
        c += 1
print(c)