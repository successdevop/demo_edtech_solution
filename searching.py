# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#
# item_to_find = "spam"
# found_at = None
#
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
# print("{0} found at position {1}".format(shopping_list[found_at], found_at))

# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#
# item_to_find = "rice"
# found_at = None
#
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
#
# if found_at is not None:
#     print("Item found at position {0}".format(found_at))
# else:
#     print("{0} not found".format(item_to_find))

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "beans"
found_at = None

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {0}".format(found_at))
else:
    print("{0} not found".format(item_to_find))
