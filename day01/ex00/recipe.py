class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        try:
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
        except ValueError:
            print("Error")

    def __str__(self):
        txt = "name:{0}\ncooking level:{1}\ncooking time:{2}\ningredients:{3}\ndescription:{4}\nrecipe_type:{5}".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)
        return txt

