expenses = []


def validate_amount(amount: str) -> int:
    while True:
        if not amount.isnumeric():
            print("Please enter a valid number as amount")
            amount = input("> ")
        else:
            break

    return int(amount)


def validate_string(string: str) -> str:
    while True:
        if not string.isalnum():
            print("Please enter a valid information")
            string = input("> ")
        else:
            break

    return string


def add_expenses() -> None:
    print("Please enter your expenses---(amount of expense, category of expense, and the description of expense)")
    while True:
        amount = input("Enter the amount: ")
        amount = validate_amount(amount)

        category = input("Enter the category: ")
        category = validate_string(category)

        desc = input("Enter the description: ")
        desc = validate_string(desc)

        data = {"amount": amount, "category": category, "desc": desc}
        expenses.append(data)
        print("Expenses added")
        print("*=*" * 25)

        condition = input("Do you want to add another expenses? YES or NO\n>: ")
        if condition == "YES".casefold():
            print("Add another expense: ")
        else:
            break


def view_expense(data: list) -> None:
    if len(data) == 0:
        print(f"No expenses: {data}")

    for index, expense_data in enumerate(data):
        print(f"{index+1}. {expense_data["category"].capitalize()} - #{expense_data["amount"]} - {expense_data["desc"]}")


def total_spending(data: list) -> None:
    output = 0
    for expense_data in data:
        output += expense_data["amount"]
    print(f"Total: #{output}")


def filter_expenses_by_category(data: list) -> None:
    category = input("Enter category: ")
    for dataset in data:
        if dataset["category"] == category:
            print(dataset)


def category_summary(data: list) -> None:
    result = {}
    for categories in data:
        if categories["category"] in result:
            result["category"] += categories["amount"]
        else:
            result["category"] = categories["amount"]

        # result["category"] = result.setdefault("category", 0) + categories["amount"]
    print(result)


def highest_expense(data: list) -> None:
    output = 0
    transaction = {}
    for h_expense in reversed(data):
        if h_expense["amount"] > output:
            output = h_expense["amount"]
            transaction = h_expense
    print(transaction)


    # for key, value in result.items():
    #     print(f"{key}: {value}")


add_expenses()
# view_expense(expenses)
# total_spending(expenses)
# filter_expenses_by_category(expenses)
# category_summary(expenses)
# highest_expense(expenses)
