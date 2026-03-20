vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}


vehicles["star fighter"] = "Lockheed F104"
vehicles["learjet"] = "Bombardier learjet"
vehicles["toy"] = "glider"
vehicles['virago'] = "Innoson iv50"

# del vehicles["success"]
result = vehicles.pop("success", "Does not exist")
print(result)
plane = vehicles.pop('fiesta')
print(plane)
bike = vehicles.pop("jimny", "check again")
print(bike)
print()
print(vehicles)

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