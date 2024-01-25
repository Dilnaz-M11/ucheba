results = input()

current_count = 0
max_count = 0

for result in results:
    if result == 'о':
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print(max_count)