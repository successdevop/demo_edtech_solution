# for i in range(1, 13):
#     print("No {:4} squared is {:4} and cubed is {:4}".format(i, i**2, i**3))
# print("*" * 45)

name = input("Please enter your name: ")
age = int(input("How old are you {} ".format(name)))

# if age is not int(age):
#     print("Please enter a number value")
# elif age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("You are not eligible to vote {}, please come back in {} years time".format(name, 18 - age))

if age < 18:
    print("You are not eligible to vote {}, please come back in {} years time".format(name, 18 - age))
elif age == 800:
    print("You are to old to vote, please pray for the voting process")
else:
    print("You are eligible to vote {}".format(name))
    print("Please put an XX in the box")
