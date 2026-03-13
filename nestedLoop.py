for i in range(1, 13):
    for j in range(1, 13):
        print("{0} and {1}".format(i, j))
    print("*="*5)

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        continue
    print(item)
