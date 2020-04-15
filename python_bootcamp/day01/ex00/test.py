import datetime
from book import Book 
from recipe import Recipe

a = Recipe("haha", 1, 10,["salad", "soup"], "disgusting thing", "lunch")
to_print = str(a)

dico = {
    'starter': {}, 
    'lunch': {'haha': a}, 
    'dessert': {}
}

book = Book("The Book", datetime.date, datetime.date, dico)

b = Recipe("hoho", 2, 20,["potatoes", "carot"], "very good stuff", "starter")

book.get_recipe_by_name("haha")
book.get_recipes_by_types("lunch")
book.add_recipe(b)
print(book.get_recipe_by_name("hoho"))