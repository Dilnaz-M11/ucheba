n = int(input())

advice_list = []

for _ in range(n):
    advice = input()
    advice_list.append(advice)

for advice in advice_list:
    if advice[:2].lower() == "не":
        print(advice[2:])
    else:
        print(advice)