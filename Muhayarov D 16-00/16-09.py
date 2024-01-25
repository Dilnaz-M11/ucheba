BASE = ["Иван", "Юлия Цезаревна"]


def hello(name):
    print('Здравствуйте,', name + '!', 'Вашу карту ищут...')


def search_card(name):

    if name in BASE:
        print('Ваша карта с номером', BASE.index(name) + 1, 'найдена')
    else:
        print('Ваша карта не найдена')


def main():
    hello("Иван")
    search_card("Иван")
    hello("Юлия Иванова")
    search_card("Юлия Иванова")


main()