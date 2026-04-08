class Car:
    car_name = "Mercedes Benz"

    def __init__(self, color: str, millage: int):
        self.color = color
        self.millage = millage

    def __str__(self):
        return f"The {self.color} car has {self.millage:,} miles"


red_car = Car("red", 30_000)
blue_car = Car("blue", 20_000)

for car in [red_car, blue_car]:
    print(car)
#
# print(blue_car)
# print(red_car)


