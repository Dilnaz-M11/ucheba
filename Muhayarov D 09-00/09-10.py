n = int(input())
a = []
flag = False
number = 0
for i in range(n):
    a.append(int(input()))
p = int(input())
q = int(input())
k = 1

for s in a:
    if k == p:
        flag = True
    if k == q:
        flag = False
        number += int(s)
    if flag:
        number += int(s)
    k += 1

print(number)