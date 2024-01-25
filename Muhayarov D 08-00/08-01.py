word = input()
longest_word = word
shortest_word = word

# считываем следующие слова, пока не встретим слово "стоп"
while word != "стоп":
    word = input()
    # обновляем значения для длиннейшего и кратчайшего слова
    if word != "стоп":
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len(shortest_word):
            shortest_word = word

# проверяем, содержатся ли все буквы кратчайшего слова в длиннейшем
contains_all_letters = True
for letter in shortest_word:
    if letter not in longest_word:
        contains_all_letters = False
        break

# выводим результат
if contains_all_letters:
    print("да")
else:
    print("нет")