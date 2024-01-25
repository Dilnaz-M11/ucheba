n = int(input())

results = []

for i in range(n):
    line = input()

    if "кот" in line:
        results.append((i + 1, line.index("кот") + 1))

for res in results:
    print(res[0], res[1])