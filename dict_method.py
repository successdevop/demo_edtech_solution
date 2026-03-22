d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is the new three"
}

d.update(d2)
print(d)
pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']
#
new_pantry = dict.fromkeys(pantry_items, 1)
# print(new_pantry)

d.update(enumerate(new_pantry))
print(d)
#
# keys = new_pantry.keys()
# print(keys)