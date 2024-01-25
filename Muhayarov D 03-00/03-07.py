def guess_number():
    low = 1
    high = 1000
    count = 1

    while count <= 10:
        mid = (low + high) // 2
        print(mid)
        response = input(">")
        if response == ">":
            low = mid + 1
        elif response == "<":
            high = mid - 1
        elif response == "=":
            print("Угадано правильно! Число попыток:", count)
            break
        count += 1

guess_number()