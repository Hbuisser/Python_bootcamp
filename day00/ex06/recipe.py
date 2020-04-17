cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': '10'
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': '60'
    },
    'salad': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'lunch',
        'prep_time': '15'
    }
}

def read(recipe):
    for key, val in cookbook.items():
        if key == recipe:
            print("Recipe for", key, end=":\n")
            print("Ingredients list: {}\nTo be eaten for {}.\nTakes {} minutes of cooking.".format(*val.values()))

def delete(recipe):
    if recipe in cookbook:
        del cookbook[recipe]

def add(recipe):
    ingredients = []
    while True:
        ingredient = input("ingredient to add (type 1 to stop):")
        if ingredient.isdigit() and int(ingredient) == 1:
            break
        elif len(ingredient) is 0:
            print("Cannot add if ingredient is empty")
            continue
        ingredients.append(ingredient)
    print("what is the kind of meal?")
    meal = input("-->")
    print("what is the prep time?")
    prep_time = input("-->")
    cookbook[recipe] = {'ingredients': ingredients, 'meal': meal, 'prep_time': prep_time}

print("Please select an option by typing the corresponding number:")
print("1: Add a recipe")
print("2: Delete a recipe")
print("3: Print a recipe")
print("4: Print the cookbook")
print("5: Quit")
a = input("-->")

if a == '1':
    print("What's the name of the recipe?")
    recipe = input("-->")
    add(recipe)
elif a == '2':
    print("wich recipe?")
    recipe = input("-->")
    delete(recipe)
elif a == '3':
    print("wich recipe?")
    recipe = input("-->")
    read(recipe)
elif a == '4'
    
elif a == '5':
    print('\n')
    print("Cookbook closed.")

print(cookbook)