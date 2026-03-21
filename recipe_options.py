recipes_tuple = {
    "Chicken and chips": [
        ("chicken", 100),
        ("potatoes", 3),
        ("salt", 1),
        ("malt vinegar", 5),
    ],
}

recipes_dict = {
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
}

#
# for recipe, qty in (recipes_tuple["Chicken and chips"]):
#     print(f"You have {qty} {"quantities" if qty > 1 else "quantity"} of {recipe}")
# for recipe, ingredient in recipes_dict.items():
#     print(f"Ingredients for {recipe}")
#     for ing, qty in ingredient.items():
#         print(ing, qty, sep=", ")
# print("+="*30)
#
# for recipe, ingredient in recipes_tuple.items():
#     print(f"Ingredients for {recipe}")
#     for val, qty in ingredient:
#         print(val, qty, sep=", ")


