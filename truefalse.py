# day = "Saturday"
# temperature = 30
# raining = True
#
# if day == "Saturday" and temperature > 27 or not raining:
#     print("Go swimming")
# else:
#     print("Learn python")
#
# print("*" * 50)
# if 1:
#     print("True")
# else:
#     print("False")
#
# if "":
#     print("Empty")
# else:
#     print("Not empty")
#
# name = input("What is your name? ")
# if name:
#     print("My name is {}".format(name))
# else:
#     print("No name")
#
# print("+=" * 50)
# parrot = "NorwegianBlue"
# letters = input("Enter your character: ")
#
# if letters != "" and letters in parrot:
#     print("True")
# else:
#     print("False")

print("Final challenge on Boolean")
name = input("Please enter your name: ")
age = int(input("Hellow {}, please enter your age: ".format(name)))

if 18 < age < 31:
    print("You are welcome to the holiday")
else:
    print("You do not qualify for the holiday, please come back after {} years".format((19 - age) if age < 19 else 0))

