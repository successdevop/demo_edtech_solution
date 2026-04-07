class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"{self.name} is {self.age} years old")

    def sound(self, sound):
        print(f"{self.name} says {sound}")


bingo = Dog("Bingo", 4)
puppy = Dog("Puppy", 6)

print(bingo)
print(puppy)
print(bingo == puppy)


