print('Добро пожаловать в Квест.')
print('Вы очнулись в темной комнате')
print('Перед вами 3 двери с номерами: 1, 2 и 3.')
print('Какую дверь выберете?')
otvet1 = input()
if otvet1 == '3':
    print('Пройдя в эту дверь, она захлопнулась')
    print('Вы оказались в комнате, которая вскоре загорелась. Не повезло')
elif otvet1 == '1':
    print('Вы прошли в бассейн с кислотой.')
if otvet1 == '2':
    print('Вы в следующей комнате')
    print('Но тут вы видите уже 2 двери, возможно за одной из них выход')
    print('Выберите дверь правая или левая')
    otvet2 = input()
    if otvet2 == 'правая':
        print('Вы смело открыли правую дверь. Но за ней вас подстерегал военком с повесткой. Хорошая попытка')
    elif otvet2 == 'левая':
        print('Вы выбрались! Победа!')