string1 = input()
string2 = input()

bulls = 0
cows = 0

for i in range(len(string1)):
    if string1[i] == string2[i]:
        bulls += 1
    elif string1[i] in string2:
        cows += 1

print(bulls, cows)