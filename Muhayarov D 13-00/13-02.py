dc = {}
for i in range(int(input())):
    val, key = input().split()
    if key in dc:
        dc[key].append(val)
    else:
        dc[key] = [val]

for i in range(int(input())):
    key = input()
    if key in dc:
        print(*dc[key])
    else:
        print('Нет в телефонной книге')