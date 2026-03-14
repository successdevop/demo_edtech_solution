computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]

another_list = computer_parts
print(id(computer_parts))
print(id(another_list))
print()
computer_parts += ["joystick"]
print(computer_parts)
print(id(computer_parts))
print(another_list)
print(id(another_list))
print()
a = b = c = d = e = another_list
print(a)
b.append("disk_drive")
print(computer_parts)
print(id(computer_parts))
print(id(a))
print(id(b))


# for part in computer_parts:
#     print(f"{computer_parts.index(part)}. "+part)
# print()
# print(computer_parts[2])
# print(computer_parts[0:3])
# print(computer_parts[-1])
