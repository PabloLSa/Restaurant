from pytest_dependency import pytest

from models.ingredient import Ingredient
from src.models.dish import Dish


# Req 2
def test_dish():
  
    dish1 = Dish("Pizza", 10.99)
    dish2 = Dish("Coca-Cola", 5.99)
    assert dish1.name == "Pizza"
    assert dish1.price == 10.99

    assert dish1 == dish1
    assert dish1 != dish2

    assert hash(dish1) == hash(dish1)
    assert hash(dish1) != hash(dish2)

    assert dish1.get_ingredients() == set()

    assert dish1.get_restrictions() == set()

    assert repr(dish1) == "Dish('Pizza', R$10.99)"

    Mussarela = Ingredient("queijo mussarela")
    dish1.add_ingredient_dependency(Mussarela, 1)
    assert dish1.get_ingredients() == {Mussarela}

    with pytest.raises(TypeError):
        Dish("Pizza", "10.99")  # type: ignore

    with pytest.raises(ValueError):
        Dish("Pizza", -10.99)
