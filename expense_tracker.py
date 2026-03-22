expenses = [
    {"amount": 2000, "category": "food", "desc": "lunch"},
    {"amount": 5000, "category": "transport", "desc": "uber"},
    {"amount": 3000, "category": "bills", "desc": "data subscription"},
    {"amount": 7000, "category": "food", "desc": "party"},
    {"amount": 9000, "category": "food", "desc": "kitchen stock up"},
    {"amount": 400, "category": "transport", "desc": "church service"},
    {"amount": 1000, "category": "bills", "desc": "electricity"},
]


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
        print("No such category")



def category_summary(data: list) -> None:
    result = {}
    for categories in data:
        category = categories["category"]
        # if category in result:
        #     result[category] += categories["amount"]
        # else:
        #     result[category] = categories["amount"]
        result[category] = result.setdefault(category, 0) + categories["amount"]

    for key, value in result.items():
        print(f"{key.capitalize()}: #{value}")


def highest_expense(data: list) -> None:
    output = 0
    transaction = {}
    for h_expense in reversed(data):
        if h_expense["amount"] > output:
            output = h_expense["amount"]
            transaction = h_expense
    print(transaction)


# add_expenses()
# print("*+"*5+"View Expenses"+"*+"*5)
# view_expense(expenses)
# print("*+"*5+"Total Expenses"+"*+"*5)
# total_spending(expenses)
# print("*+"*5+"Expense by Category"+"*+"*5)
# filter_expenses_by_category(expenses)
# print("*+"*5+"Category Expense Summary"+"*+"*5)
# category_summary(expenses)
# print("*+"*5+"Highest Expense Transaction"+"*+"*5)
# highest_expense(expenses)

def main():
    while True:
        options = "1234560"
        print("Welcome to your expense tracker, choose your option")
        print("1. Add expenses")
        print("2. View expenses")
        print("3. View expenses by category")
        print("4. View expense summary")
        print("5. View highest expense transaction")
        print("6. Total expenses")
        print("0. Exit")

        choice = input(": ")
        if choice not in options:
            print("Please enter a valid option")
        else:
            if choice == "1":
                add_expenses()
                print()
            elif choice == "2":
                view_expense(expenses)
                print()
            elif choice == "3":
                filter_expenses_by_category(expenses)
                print()
            elif choice == "4":
                category_summary(expenses)
                print()
            elif choice == "5":
                highest_expense(expenses)
                print()
            elif choice == "6":
                total_spending(expenses)
                print()
            elif choice == "0":
                break


main()
