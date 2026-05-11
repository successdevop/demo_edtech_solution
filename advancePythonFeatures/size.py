import sys

# big_range = range(1000)
def my_range(n: int):
    print("my range starts")
    start = 0
    while start < n:
        print("my range is returning {}".format(start))
        yield start
        start += 1

# _ = input("line 12")
big_range = my_range(5)
_ = input("line 14")

print(next(big_range))
print(next(big_range))
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

big_list = []

_ = input("line 19")
for val in big_range:
    _ = input("line 21 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))

print(big_range)
print(big_list)