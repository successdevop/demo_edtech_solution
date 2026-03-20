available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "mouse mat",
    "6": "hdmi cable",
    "7": "card reader"
}
print(available_parts)

current_choice = None
computer_parts = []

while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
            print()
        else:
            print(f"Adding ({chosen_part})")
            computer_parts.append(chosen_part)
            print(f"Your list now contains: {computer_parts}")
            print("*=+"*10)
    else:
        print("Choose from the available items: ")
        for key, values in available_parts.items():
            print(f"{key}. {values}")
        print("0. To exit")
    current_choice = input("> ")


