animals = {
    "lion": ["scary","big","cat"],
    "elephant": ["big","grey","wrinkled"],
    "teddy": ["cuddly", "stuffed"]
}


new_animal = {}
for k, v in animals.items():
    new_animal[k] = new_animal.setdefault(k, v)

print(new_animal)
print(animals)
print(id(new_animal))
print(id(animals))

new_animal["lion"].append("carnivorous")
print(new_animal)
print(animals)


# things = animals.copy()
# print(things["teddy"])
# print(animals["teddy"])
#
# print(id(animals))
# print(id(things))
# print()
# things["teddy"].append("toy")
# print(things["teddy"])
# print(animals["teddy"])
# print(id(animals))
# print(id(things))


