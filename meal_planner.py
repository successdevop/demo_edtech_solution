from content import pantry, recipes
#
# print(pantry)
# print(recipes)


def display_recipe(data: dict) -> dict:
    new_data = {}
    for key, value in enumerate(data):
        new_data[str(key + 1)] = value
    return new_data


def display_recipe_ingredients(string: str) -> None:
    for key, value in enumerate(recipes[string]):
        print(f"{key+1} - {value}")

# display_recipe_ingredients("Pizza")


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
        print()
        print(f"These are the ingredients of {item_selected}")
        display_recipe_ingredients(item_selected)
