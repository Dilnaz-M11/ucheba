names = [input() for _ in range(int(input()))]
k, m = int(input()), int(input())
for _ in range(m):
    del names[k-1::k]
for name in names:
    print(name)