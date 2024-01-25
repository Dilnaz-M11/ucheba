sum = 0
c = 0
a = int(input())
while a != 0:
    sum += a
    if sum <= 10 or sum < 0:
        c += 1
    a = int(input())
print(c)
