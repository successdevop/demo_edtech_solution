# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# found_at = None
#
# if "albatross" in shopping_list:
#     found_at = shopping_list.index("albatross")
#
# if found_at is not None:
#     print("Item found at position {0}".format(found_at))
# else:
#     print("{0} not found".format("albatross"))
#
# i = 10
# while i >= 0:
#     print("i is now {0}".format(i))
#     i = i - 1
# print("+="*10)
#
# j = 0
# while j <= 10:
#     print(f"j is now {j}")
#     j += 1

# available_exit = ["north", "south", "east", "west"]
# chosen_exit = ""
#
# while chosen_exit.casefold() not in available_exit:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit.casefold() == "quit":
#         break
#
# if chosen_exit in available_exit:
#     print("Thank God you found your way out")
# else:
#     print("Quiting is not always a bad plan")

available_exit = ["north", "south", "east", "west"]
chosen_exit = ""

while True:
    if chosen_exit.casefold() != "quit" and chosen_exit.casefold() not in available_exit:
        chosen_exit = input("Please choose a direction: ")
    elif chosen_exit.casefold() == "quit":
        print("Quiting is not always a bad plan")
        break
    else:
        print("Thank God you found your way out")
        break


