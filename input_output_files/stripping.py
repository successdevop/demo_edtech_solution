filename = "Jabberwocky.txt"

with open(filename) as poem:
    first = poem.readline().strip()

print(first)

char = "' Twasebv"
# no_apostrophe = first.strip(char)
# print(no_apostrophe)

# for character in first:
#     if character in char:
#         print(f"Removing {character}")
#     else:
#         break