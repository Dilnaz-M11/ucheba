a = int(input())
m = []
f = 0
for i in range(a):
    b = int(input())
    m.append(b)
final = int(input())
for i in range(a):
    for k in range(i + 1, a):
        if final == m[i] * m[k]:
            f = 1
if f == 1:
    print("ДА")
else:
    print("НЕТ")