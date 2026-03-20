import random


def get_integer(prompt):
    """
    this function would continue loping and prompting the user until a valid 'int' is entered
    The function returns an int from the user input
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print(f"{temp} is not a valid number")


highest = 10
answer = random.randint(1, highest)
guess = 0
print(f"Please guess between 1 and {highest}:")

while answer != guess:
    guess = get_integer(": ")

    if guess == 0:
        break

    if guess == answer:
        print("You guessed it correctly")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")

