def caesar_cipher(shift, message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

shift = int(input())  # вводим шаг шифрования
message = input()  # вводим послание
encrypted_message = caesar_cipher(shift, message)
print(encrypted_message)