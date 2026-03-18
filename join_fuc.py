# flowers = ["Daffodil", "Evening Primrose",
#            "Hydrangea", "Iris", "Lavender",
#            "Sunflower", "Tiger Lily"
#            ]
#
# seperator = " ** "
# output = seperator.join(flowers)
# print(output)
# print()
# print(", ".join(flowers))

#
# pangram = "The quick brown fox jumps over the lazy dog"
# print(pangram.split())

# numbers = "9,223,372,036,854,775,807"
# value_list = "".join(numbers).split(",")
# value_list = [int(val) for val in value_list]
# print(value_list)
#
# list_box = []
# for val in numbers:
#     if val.isnumeric():
#         list_box.append(int(val))
# print(list_box)

# value = numbers.split(",")
# empty = []
# for val in value:
#     val = int(val)
#     empty.append(val)
# print(empty)
new_number = []
number = input("Please enter three numbers, separated by commas: ")
while True:
    number = number.split(",")
    if len(number) == 3:
        for val in number:
            if val.lstrip("-").isdigit():
                new_number.append(int(val))
                print(new_number)
        output = new_number[0] + new_number[1] - new_number[2]
        print(output)
        break
    else:
        number = input("Please enter three numbers, separated by commas: ")
