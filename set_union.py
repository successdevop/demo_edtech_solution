from precription_data import *

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

all_animals_1 = farm_animals.union(wild_animals)
# print(all_animals_1)

all_animals_2 = wild_animals.union(farm_animals)
# print(all_animals_2)

all_animals_3 = farm_animals | wild_animals
# print(all_animals_3)

med_in_new_set = {*{}}

# for drugs in adverse_interactions:
#     # med_in_new_set = med_in_new_set.union(drugs)
#     # med_in_new_set = med_in_new_set | drugs
#     # med_in_new_set.update(drugs)
#     med_in_new_set |= drugs

med_in_new_set.update(*adverse_interactions)

print(med_in_new_set)

scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}

# biters = scorpions.union(spiders)
# print(biters)
# scorpions |= spiders
# print(scorpions)
# print()
# stingers = snakes.union(vespas)
# print(stingers)
# snakes |= vespas
# print(snakes)
