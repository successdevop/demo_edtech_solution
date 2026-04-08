class Dog:
    species = "Canis familiaris"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound: str):
        return f"{self.name} barks: {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound = "Arf"):
        return f"{self.name} says {sound}"


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


miles = JackRussellTerrier("Miles", 4)
buddy = Bulldog("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Dachshund("Jim", 5)

# print(isinstance(miles, Dog))
# print(isinstance(miles, JackRussellTerrier))
print(miles.speak("Grrr"))
print(jim.speak("Woof woof"))


class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(f"{self.brand}")

# Create an object
c1 = Car("Ford")

# Call the show method
c1.show()