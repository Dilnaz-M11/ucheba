print('Любите ли вы компьютеры? Ответьте - да или нет.')
question1 = input()
print('Умеете ли вы программировать? Ответьте - да или нет.')
question2 = input()
if question1 == 'да' and question2 == 'да':
    print('Отлично! Да вы прирожденный программист!')
elif question1 == 'нет' and question2 == 'нет':
    print('Увы и ах')
elif question1 == 'да' and question2 == 'нет':
    print('Советую научиться')
elif question1 == 'нет' and question2 == 'да':
    print('Компьютеры и программирование - это неразделимые вещи :)')
else:
    print('Что-то пошло не так! Пройдите тест заново.')