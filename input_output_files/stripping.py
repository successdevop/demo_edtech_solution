filename = "Jabberwocky.txt"

with open(filename) as poem:
    first = poem.readline().strip()

print(first)
print()

# char = "' Twasebv"
# no_apostrophe = first.strip(char)
# print(no_apostrophe)

# for character in first:
#     if character in char:
#         print(f"Removing {character}")
#     else:
#         break


def remove_prefix(string:str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]


def remove_suffix(string:str, suffix:str) -> str:
    if string and string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]


print(remove_prefix(first, "'Twas"))
print()
print(remove_suffix(first, "'Twas"))
