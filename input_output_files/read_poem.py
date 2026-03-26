# jabber = open("Jabberwocky.txt", "r")
#
# for lines in jabber:
#     print(lines.strip())
#
# jabber.close()

# with open("Jabberwocky.txt", "r") as Jabber:
#     for lines in Jabber:
#         print(lines.strip())

# with open("Jabberwocky.txt", "r") as jab:
#     lines = jab.readlines()
#
# for line in reversed(lines):
#     print(line.strip())

# with open("Jabberwocky.txt") as jab:
#     lines = jab.read()
#
# for char in reversed(lines):
#     print(char, end="")

with open('Jabberwocky.txt') as word_file:
    for line in word_file:
        print(line.strip())
        if 'jubjub' in line.casefold():
            break

print("*=" * 50)

with open('Jabberwocky.txt') as success:
    while True:
        line = success.readline().rstrip()
        print(line)
        if "jubjub" in line.casefold():
            break
