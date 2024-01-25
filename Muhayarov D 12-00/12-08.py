n = input("Введите шифр: ")
n.strip()
a = 0
b = 0
c = 0
for i in range(len(n)):
    a = n.count(n[i])
    if a > b:
        c = i
    b = a
print(n[c])