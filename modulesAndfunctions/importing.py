from bad_code import area_of_square, area_of_square_2

result = area_of_square_2(23)
print(result)

out = area_of_square(30)
print(out)

print("Global namespace")
namespace = globals().copy()
for name, obj in namespace.items():
    print(f"{name} - {obj}")