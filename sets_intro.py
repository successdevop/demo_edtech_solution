farms_animals = {"cow", "sheep", "hen", "goat", "horse"}

# numbers = {*{}}
# print(numbers)
#
# number = {*""}
# print(number)
#
# new_numbers = set()
# print(new_numbers)
#
# new_numbers.add(3)
# print(new_numbers)
# print("+"*15)
#
# while len(numbers) < 4:
#     val = input("Enter number: ")
#     numbers.add(val)
#
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]
# print(data)
# print()
#
# data_1 = sorted(set(data))
# print(data_1)
# print()
#
data_2 = set(dict.fromkeys(data))
print(data_2)

data_2.discard("red")
print(data_2)

data_2.remove("pink")
