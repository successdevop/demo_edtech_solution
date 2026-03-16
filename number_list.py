even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# even.extend(odd)
# print(even)
# even.sort()
# print(even)
# even.reverse()
# print(even)

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
# print()
# print(len(even))
# print(len(odd))
# print()
# print(even.count(2))
# print("mississippi".count("ssi"))

pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
print(numbers)
another_number = sorted(numbers)
print(another_number)
print()
another_number = numbers.sort()
print(another_number)
print(numbers)
print()
missing_letters = sorted("The quick brown fox jumped over the lazy dog",key=str.casefold)
print(missing_letters)

names = ["Graham", "John", "terry", "eric", "Terry", "michael"]
print(names)
names.sort(key=str.casefold)
print(names)
print()
new_names = sorted(names)
print(new_names)