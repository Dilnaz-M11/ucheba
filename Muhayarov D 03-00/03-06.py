password = input("Введите пароль: ")
confirm_password = input("Подтвердите пароль: ")

# Пока пароли не совпадают или не удовлетворяют условиям, продолжаем запрашивать пароли
while password != confirm_password or len(password) < 8 or "123" in password:
    # Если пароль короткий, выводим сообщение
    if len(password) < 8:
        print("короткий!")
    # Если пароль содержит "123", выводим сообщение
    elif "123" in password:
        print("простой!")
    # Если пароли не совпадают, выводим сообщение
    elif password != confirm_password:
        print("различаются.")

    # Снова считываем пароль и подтверждение пароля от пользователя
    password = input("Введите пароль: ")
    confirm_password = input("Подтвердите пароль: ")

# Если все условия выполнены, выводим "ok"
print("ok")