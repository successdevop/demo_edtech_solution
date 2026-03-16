# computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]
#
# print(computer_parts)
# computer_parts[3] = "trackball"
# print(computer_parts)
# computer_parts[3:] = "trackball"
# print(computer_parts)
# computer_parts[3:] = ["trackball"]
# print(computer_parts)

# data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
# data = [4,5,104,105,110,120,130,130,150,160,170,183,185,187,188,191]
# data = [104,105,110,120,130,130,150,160,170,183,185,187,188,191,350,360]
# data = [1041,1051,1101,1201,1301,1301,1501,1601,1701,1831,1851,1871,1881,1911]
data = []




# del data[0:2]
# print(data)
# del data[-2:]
# print(data)

min_val = 100
max_val = 200
stop = 0
for index, value in enumerate(data):
    if value >= min_val:
        stop = index
        break
print(stop)
del data[:stop]
print(data)

stop = 0
for index, value in enumerate(data):
    if value >= max_val:
        stop = index
        break
print(stop)
del data[14:]
print(data)
print("=+"*5)
