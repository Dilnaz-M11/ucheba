sum = 0
for i in range(1, int(input()) + 1):
    if i % 2 != 0:
        sum += int(input())
    else:
        sum -= int(input())
print(sum)