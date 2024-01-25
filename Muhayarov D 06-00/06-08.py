n = int(input())
surname = set()
double = set()
a = 0
for i in range(n):
    name = input()
    if name not in surname:
        surname.add(name)
    else:
        a += 1
        if name not in double:
            double.add(name)
a += len(double)
print(a)