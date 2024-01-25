s = input()
for char in s:
    if not (char.islower() or char.isdigit() or char == "_"):
        print("неверный символ:", char)
        break
else:
    print("ok")