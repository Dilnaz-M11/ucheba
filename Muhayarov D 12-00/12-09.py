n = input()
print(*[i for i in input().split() if n.upper() in i or n in i],sep='\n')