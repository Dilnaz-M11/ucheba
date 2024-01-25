PHRASES = []
def parrot(phrase):
    if phrase not in PHRASES:
        PHRASES.append(phrase)
    else:
        print(phrase)


parrot("Привет!")
parrot("Привет!")
parrot("Как дела?")