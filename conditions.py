age = int(input("How old are you? "))

# if age >= 16 and age <= 64:
if 16 <= age <= 65:
    print("Have a good day at work")
print("=" * 50)

if age < 16 or age > 65:
    print("Not eligible for work")
else:
    print("Have a good day at work")
