from services.inventory_control import InventoryMapping
from services.menu_data import MenuData


class MenuBuilder:
    def __init__(self, data_path, inventory_path):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def get_main_menu(self, restriction=None):
        def is_dish_available(dish):
            return (
                not (restriction and restriction in dish.get_restrictions())
                and all(self.inventory.inventory.get(ingredient, 0) > 0 for ingredient in dish.get_ingredients())
            )

        menu = [
            {
                "dish_name": prato.name,
                "ingredients": prato.get_ingredients(),
                "price": prato.price,
                "restrictions": prato.get_restrictions(),
            }
            for prato in self.menu_data.dishes
            if is_dish_available(prato)
        ]

        return menu

