size = int(input())

for i in range(size, 0, -1):
    for j in range(ord('A'), ord('A') + size):
        print(chr(j) + str(i), end=" ")
    print()