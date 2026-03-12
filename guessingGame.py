answer = 5
print("Please enter the number:")
guess = int(input())

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done You guessed it correctly")
    else:
        print("You have guessed wrongly")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done You guessed it correctly")
    else:
        print("You have guessed wrongly")
else:
    print("You got it on first guess")
