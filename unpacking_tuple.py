# a = b = c = d = e = f = 12
# print(d)
# x, y, z = 1, 2, 76
# print(x)
# print(y)
# print(z)
# print()
# data = 1, 2, 76
# print(data)
# print()
# x, y, z = data
# print(x)
# print(y)
# print(z)
# print()
#
# data_list = [12, 13, 14]
# data_list.append(15)
#
# p, q, r = data_list
# print(p)
# print(q)
# print(r)

for index, character in enumerate("abcdefgh"):
    print(index, character)

print("+="*25)
for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)
