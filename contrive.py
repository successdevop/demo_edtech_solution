# numbers = [3, 8, 11, 17, 29, 43, 16, 83]
# position_at = None
# for number in numbers:
#     if number % 12 == 0:
#         position_at = number;
#         print(f"{position_at} is divisible by 8")
#         print("List is unaccepted")
#         break
# else:
#     print("The list is acceptable")


options_list = ["Exit", "Learn Python", "Learn Java", "Go swimming", "Have dinner", "Go to bed"]
while True:
    print("Please choose your option from the list below:")
    for val in range(len(options_list)):
        print(f"{val}. {options_list[val]}")

    user_input = int(input("Enter option number: "))
    if user_input > len(options_list) - 1:
        print("+=" * 20)
        continue
    else:
        if user_input == 0:
            print("Thank you for exiting the program")
            break
        else:
            print(f"Number {user_input} was chosen, please ({options_list[user_input]})")
            print("+="*20)

