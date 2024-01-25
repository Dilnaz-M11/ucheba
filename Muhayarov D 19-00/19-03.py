numbers = filter(lambda x: x % 9 == 0 and x > 9 and x < 100, range(1, 100))
squares = map(lambda x: x**2, numbers)
result = sum(squares)
print(result)