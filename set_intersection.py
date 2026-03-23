trial_1 = {"Bob", "Charlie", "Georgia", "John"}
trial_2 = {"Anne", "Charlie", "Eddie", "Georgia"}

check_set = trial_1.intersection(trial_2)
# print(check_set)
check_set_1 = trial_1 & trial_2
# print(check_set_1)
trial_1 &= trial_2
# print(trial_1)

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
potential_rides = {"donkey", "horse", "camel"}

farm_animals &= wild_animals & potential_rides
abc = farm_animals & wild_animals
# print(abc)

# print(farm_animals)

bcd = farm_animals.intersection(wild_animals, potential_rides)
# print(bcd)

text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.
quote = set(text.split())
preps_used = prepositions & quote
print(preps_used)