n = int(input("Введите кол-во клиентов: "))
list = []
for i in range(n):
    m = int(input("Введите кол-во накоплений клинта: "))
    list.append(m)
    print(list[i])
print("")

for k in range(len(list)):
    list[k] *= 3

for c in list:
    print(c)