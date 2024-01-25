m = int(input())  # количество продуктов
fridge = set()

# продукты
for _ in range(m):
    product = input()
    fridge.add(product)

n = int(input())
recipes = []

# о рецептах
for _ in range(n):
    recipe_name = input()
    num_ingredients = int(input())
    ingredients = set()

    for _ in range(num_ingredients):
        ingredient = input()
        ingredients.add(ingredient)

    if ingredients.issubset(fridge):
        recipes.append(recipe_name)

for recipe in recipes:
    print(recipe)