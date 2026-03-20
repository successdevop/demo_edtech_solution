# vehicles = {
#     'dream': 'Honda 250T',
#     'roadster': 'BMW R1100',
#     'er5': 'Kawasaki ER5',
#     'can-am': 'Bombardier Can-Am 250',
#     'virago': 'Yamaha XV250',
#     'tenere': 'Yamaha XT650',
#     'jimny': 'Suzuki Jimny 1.5',
#     'fiesta': 'Ford Fiesta Ghia 1.4',
# }
#
#
# vehicles["star fighter"] = "Lockheed F104"
# vehicles["learjet"] = "Bombardier learjet"
# vehicles["toy"] = "glider"
# vehicles['virago'] = "Innoson iv50"
#
# # del vehicles["success"]
# result = vehicles.pop("success", "Does not exist")
# print(result)
# plane = vehicles.pop('fiesta')
# print(plane)
# bike = vehicles.pop("jimny", "check again")
# print(bike)
# print()
# print(vehicles)
import random

# for key, value in vehicles.items():
#     print("{}: {}".format(key, value))

# for key in vehicles:
#     print(f"{key}: {vehicles[key]}")

# my_car = vehicles['dream']
# print(my_car)
# commuter = vehicles['virago']
# print(commuter)
# learner = vehicles.get("er5")
# print(learner)

available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "mouse mat",
    "6": "hdmi cable",
    "7": "card reader"
}

my_choice = None
bought_computer_parts = {}

while my_choice != "0":
    if my_choice in available_parts:
        intended_part_to_buy = available_parts[my_choice]

        if intended_part_to_buy in bought_computer_parts.values():
            for key, value in bought_computer_parts.items():
                if intended_part_to_buy == value:
                    print(f"Removing: {intended_part_to_buy}")
                    del bought_computer_parts[key]
                    break
        else:
            dict_index = random.randint(1, 100)
            if dict_index not in bought_computer_parts:
                print(f"Adding ({intended_part_to_buy})")
                bought_computer_parts[dict_index] = intended_part_to_buy
        print(f"Your new list is: {bought_computer_parts}")
    else:
        print("Please choose from available options")
        for num, item in available_parts.items():
            print(f"{num}. {item}")
        print("0. To exit")
    my_choice = input("> ")

print(bought_computer_parts)