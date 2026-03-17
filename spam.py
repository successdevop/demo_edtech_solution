menu = [
    ["egg", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "sausage", "bacon"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

# for meal in menu:
#     for key, item in enumerate(reversed(meal)):
#         if item == "spam":
#             meal.remove(item)
#     print(meal)

for meal in menu:
    for index in range(len(meal)-1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)
