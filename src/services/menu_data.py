import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            reader = csv.DictReader(file)
            dish_dict = {}
            ingredient_dict = {}

            for row in reader:
                dish_name = row["dish"]
                price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                if dish_name not in dish_dict:
                    dish = Dish(dish_name, price)
                    dish_dict[dish_name] = dish
                else:
                    dish = dish_dict[dish_name]

                if ingredient_name not in ingredient_dict:
                    ingredient = Ingredient(ingredient_name)
                    ingredient_dict[ingredient_name] = ingredient
                else:
                    ingredient = ingredient_dict[ingredient_name]

                dish.add_ingredient_dependency(ingredient, recipe_amount)

        self.dishes = set(dish_dict.values())
