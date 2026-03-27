
# print("*=" * 50)
#
# with open('Jabberwocky.txt') as success:
#     while True:
#         line = success.readline().rstrip()
#         print(line)
#         if "jubjub" in line.casefold():
#             break

with open('Jabberwocky.txt', encoding='utf-8') as word_file:
    for line in word_file:
        print(line.strip())


