class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def sound(self, sound: str):
        print(f"{self.name} says {sound}")


bingo = Dog("Bingo", 4)
bingo.sound("'wooooo'")
print(bingo)

puppy = Dog("Puppy", 6)
#
# print(bingo)
# print(puppy)
# print(bingo == puppy)
#
#
