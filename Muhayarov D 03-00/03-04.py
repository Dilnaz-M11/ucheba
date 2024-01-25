input_string = ''
while True:
    user_input = input()
    if user_input == '':
        break
    input_string += user_input + '\n'

print(input_string)