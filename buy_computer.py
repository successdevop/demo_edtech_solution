# current_choice = "-"
# computer_parts = []
#
# while current_choice != "0":
#     if current_choice in "123456":
#         print(f"Adding {current_choice}")
#         if current_choice == "1":
#             computer_parts.append("computer")
#         elif current_choice == "2":
#             computer_parts.append("monitor")
#         elif current_choice == "3":
#             computer_parts.append("keyboard")
#         elif current_choice == "4":
#             computer_parts.append("mouse")
#         elif current_choice == "5":
#             computer_parts.append("mouse mat")
#         elif current_choice == "6":
#             computer_parts.append("hdmi cable")
#     else:
#         print("Please add only option from the list below: ")
#         print("1. computer")
#         print("2. monitor")
#         print("3. keyboard")
#         print("4. mouse")
#         print("5. mouse mat")
#         print("6. hdmi cable")
#     current_choice = input()
# print(computer_parts)


available_parts = ["to finish", "computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable", "card reader"]
current_choice = "-"
computer_parts = []

while current_choice != "0":

    if current_choice.isnumeric():
        index = int(current_choice)
        if index < len(available_parts):
            part = available_parts[index]

            if part in computer_parts:
                computer_parts.remove(part)
                print(computer_parts)
                print("+="*25)
            else:
                if part not in computer_parts:
                    computer_parts.append(part)
                    print(computer_parts)
                    print("+="*25)

    print("Please add only option from the list below: ")
    for val in range(1, len(available_parts)):
        print(f"{val}. {available_parts[val]}")
    print(f"{available_parts.index("to finish")}. exit")

    current_choice = input()
