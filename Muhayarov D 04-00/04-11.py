c = int(input())
a = int(input())
print(0)
for i in range(c - 1):
    num = int(input())
    a = (a + num) / 2
    if num == a:
        print(0)
    elif num < a:
        print("<")
    elif num > a:
        print(">")