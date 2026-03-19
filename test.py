import random


# def binary_search():
#     LOW, HIGH = 1, 200
#     answer = random.randint(LOW, HIGH)
#
#     guess_count = 0
#     while True:
#         guess = LOW + (HIGH - LOW) // 2
#
#         if answer > guess:
#             LOW = guess + 1
#         elif answer < guess:
#             HIGH = guess - 1
#
#         if answer == guess:
#             print("You got it at the {} guess".format(guess_count))
#             break
#
#         guess_count += 1
# binary_search()

# For this exercise, you'll write a function that returns the appropriate response, in the game of fizz buzz.
#
# It's a simple game, usually played with 2 or more people.
#
# You start counting, in turn. That's easy enough, but there's a complication.
#
# If the number is divisible by 3, you say "fizz" instead.
#
# If it's divisible by 5, you say "buzz".
#
# And if it's divisible by both 3 and 5, you say "fizz buzz".
#
#
#
# The function must be called fizz_buzz
#
#
#
# Your fizz_buzz function should return the correct word ("fizz", "buzz" or "fizz buzz"), or the number if it's not divisible by either 3 or 5.
#
# The function will always return a string. When you return the number, therefore, you should convert it to a string first.
#
#
#
# Remember to annotate your function, and include a Docstring.
#
#
#
# Include a for loop, to test your function for values from 1 to 100, inclusive.


def fizz_buzz(n: int) -> str:
    if not n.is_integer():
        return "Enter a valid number"

    output = ""

    if n % 3 == 0 and n % 5 == 0:
        output = "fizz buzz"
    elif n % 3 == 0:
        output = "fizz"
    elif n % 5 == 0:
        output = "buzz"
    else:
        output += "{}".format(n)

    return output


# print(fizz_buzz(23))

# for val in range(1, 100+1):
#     print(fizz_buzz(val))

next_number = 0
while next_number < 100:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("You go: ")
    if player_answer != correct_answer:
        print("You lose, the correct answer is {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))
