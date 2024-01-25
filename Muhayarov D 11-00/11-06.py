n = int(input("Введите количество пунтков рецепта: "))
recipe_list = []
for i in range(n):
    recipe = input()
    if "лук" not in recipe:
        recipe_list.append(recipe)
print(",".join(recipe_list))