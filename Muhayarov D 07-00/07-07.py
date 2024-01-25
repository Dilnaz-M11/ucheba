message = input("Введите сообщение: ")
encoded_message = [str(ord(char)) for char in message]
result = ",".join(encoded_message)
print(result)