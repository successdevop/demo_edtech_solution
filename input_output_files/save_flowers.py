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

flower_list = []

# with open("flowers_print.txt") as flowers:
#     for flower in flowers:
#         flower_list.append(flower.rstrip())
#
# print(flower_list)
# print("+="*80)

# plants_filename = "flowers_print.txt"
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         print(plant, file=plants)


# plant_text = "flower_shrubs.txt"
# with open(plant_text, "w") as jab_flower:
#     for plants in data:
#         print(plants, file=jab_flower)

new_plant_list = []
with open("flower_shrubs.txt") as jab_flower:
    for plant in jab_flower:
        new_plant_list.append(plant.rstrip())

print(new_plant_list)
