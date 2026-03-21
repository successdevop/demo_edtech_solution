from content import pantry, recipes
from recipe_options import recipes_tuple

# print(recipes_tuple)
# print(pantry)
# print(recipes)


def display_recipe(data: dict) -> dict:
    new_data = {}
    for key, value in enumerate(data):
        new_data[str(key + 1)] = value
    return new_data


def display_recipe_ingredients(string: str) -> dict:
    return recipes[string]


def add_items(data:dict, item:str, qty: int) -> None:
    # if item in data:
    #     data[item] += qty
    # else:
    #     data[item] = qty
    data[item] = data.setdefault(item, 0) + qty


items_to_be_bought = {}
choice = None
while choice != "0":
    print("Please choose your recipe")
    print("-"*26)
    data = display_recipe(recipes)

    for index, value in data.items():
        print(f"{index} - {value}")
    choice = input("> ")

    if choice in data:
        item_selected = data[choice]
        print(f"You have selected: {item_selected}")
        ingredients_list = display_recipe_ingredients(item_selected)
        print(f"These are the ingredients of {item_selected}: {ingredients_list}")
        print()
        # checking if our ingredients is available in our pantry list
        for food_item, required_qty in ingredients_list.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_qty <= quantity_in_pantry:
                print(f"{food_item} - \tavailable and enough")
            else:
                needed_quantity = required_qty - quantity_in_pantry
                add_items(items_to_be_bought, food_item, needed_quantity)
                print(f"You need to buy {needed_quantity} of {food_item}")
    print(items_to_be_bought)


