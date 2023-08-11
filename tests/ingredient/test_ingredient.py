from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():

    ingredient1 = Ingredient("queijo parmesão")
    ingredient2 = Ingredient("bacon")
    ingredient3 = Ingredient("presunto")

    assert ingredient1.name == "queijo parmesão"
    assert ingredient2.name == "bacon"
    assert ingredient3.name == "presunto"

    assert ingredient1 != ingredient2
    assert ingredient1 == ingredient1

    assert hash(ingredient1) == hash(ingredient1)
    assert hash(ingredient1) != hash(ingredient2)

    assert repr(ingredient1) == "Ingredient('queijo parmesão')"

    assert ingredient1.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
