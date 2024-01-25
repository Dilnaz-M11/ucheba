n = input().lower()
a = 0
for i in range(len(n)):
    if n.count(n[i]) > a:
        a = n.count(n[i])
print(a)