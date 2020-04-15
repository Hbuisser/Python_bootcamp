class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        try:
            self.name = name
            self.last_update = last_update
            self.creation_date = creation_date
            self.recipes_list = recipes_list
        except ValueError:
            print("Error")
    
    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for key,val in self.recipes_list.items():
            for key1,val1 in val.items():
                if key1 == name:
                    print(str(val1))

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """ 
        for key,val in self.recipes_list.items():
            if key == recipe_type:
                for key1,val1 in val.items():
                    print(str(val1))
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update""" 
        for key,val in self.recipes_list.items():
            if key == recipe.recipe_type:
                self.recipes_list[key][recipe.name] = recipe
