# asteroids = [9617, 9618, 9619, 9620, 9621, 9622, 13681]
#
# for asteroid in asteroids:
#     if asteroid == 9617:
#         print("Grahamchapman")
#     elif asteroid == 9618:
#         print("Johncleese")
#     elif asteroid == 9619:
#         print("Terrygilliam")
#         break
#     elif asteroid == 9620:
#         print("Ericidle")
#     elif asteroid == 9621:
#         print("Michaelpalin")
#     else:
#         print("Terryjones")
# else:
#     print("MontyPython")
#
# We have some data that contains a mixture of flowers and shrubs, in a list.
# Our customer would like two separate lists.
# One, called flowers, will contain only flowers, and the other, not surprisingly called shrubs, must contain only shrubs.
# Write code to populate the two lists with the appropriate plants from data.
# The strings in the lists should remain unchanged. If you decide to delete " - Flower" and " - Shrub" from the strings,
# that's a great improvement but isn't required to complete this exercise. But be warned, the on-line checker will
# fail your code if you attempt to delete those redundant characters but leave a trailing space in the strings.
#
# Write your code below the comment, starting on line 27.
#
# There is no need to print the lists, but you can if you wish.
#
# Hint: Note that "flower" will not match "Flower" (with a capital F) in Python.
data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

for val in data:
    if "Shrub" in val:
        shrubs.append(val)
    else:
        flowers.append(val)

print("Flowers")
print(flowers)
print("Shrubs")
print(shrubs)
