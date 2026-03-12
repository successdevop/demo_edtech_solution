# number = "9,223,372;036 854,775;807"
number = input("Enter a lsit of numbers and symbols of your choice: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators += char

print(separators)

# seperators = number[1::4]
# print(seperators)
#
value = "".join(char if char not in separators else " " for char in number).split()
print(value)
newValue = [int(val) for val in value]
print(newValue)
print(sum(newValue))


