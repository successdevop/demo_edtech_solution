animals = {"Turtle", "Horse", "Robin", "Python", "Swallow", "Hedgehog", "Wren", "Aardvark", "Cat"}

birds = {"Robin", "Swallow", "Wren"}

print(f"birds is a subset of animals: {birds <= animals}")
print(f"birds is a proper subset of animals: {birds < animals}")

print(f"animal is a superset of birds: {animals >= birds}")
print(f"animal is a proper superset of birds: {animals > birds}")
print()

print(f"birds is a superset of animals: {birds > animals}")
print(f"birds is a proper superset of animals: {birds > animals}")

print(f"animal is a subset of birds: {animals <= birds}")
print(f"animal is a proper subset of birds: {animals < birds}")