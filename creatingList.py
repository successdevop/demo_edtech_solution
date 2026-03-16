names = ["Graham", "John", "terry", "eric", "Terry", "michael"]
# print(names)
empty_list = []
even = [2,4,6,8]
odd = [1,3,5,7,9]
numbers = even + odd
print(numbers)
numbers.sort()
print(numbers)
print()
another_num = sorted(numbers)
print(another_num)
print(numbers is another_num)
print(numbers == another_num)
print()
more_number = numbers[:]
print(more_number)
print()

digits = "432985617"
new_digit = sorted(digits)
print(new_digit)
print()
another_digit = list(digits)
print(another_digit)
print()
digit_two = new_digit.copy()
print(digit_two)