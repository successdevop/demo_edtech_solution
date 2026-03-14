# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break
import random

# i = 0
# while i < 100:
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break
#     i += 7
#
# Write a program to print out all the numbers from 0 to 20 that aren't divisible by either 3 or 5.
# Zero is considered divisible by everything (zero should not appear in the output).
# The aim is to use the continue statement, but it's also possible to do this without continue.

# j = 0
# while j <= 20:
#     if j % 3 != 0 and j % 5 != 0:
#         print(j)
#     j += 1
# #
# print("="*30)

# for i in range(1, 20):
#     if i % 3 != 0 and i % 5 != 0:
#         print(i)

print("="*25)
computerNumber = random.randint(1, 10)
print(computerNumber)
guessedNumber = int(input("Please choose a number between 1 - 10: "))
gamePlayTime = 3
gameCount = gamePlayTime

while gameCount:
    if guessedNumber == 0:
        print("You ended the game....play again")
        break

    if guessedNumber == computerNumber:
        print("You got it right on the first guess")
        break
    else:
        if guessedNumber < computerNumber:
            print("Please guess higher")
        else:
            print("Please guess lower")
        guessedNumber = int(input())
        if guessedNumber == computerNumber:
            print("Well done, you have guessed correctly")
            break

    gameCount -= 1
    if gameCount == 0:
        print(f"GAME OVER...you can only play {gamePlayTime} times")



# while True:
#     if guessedNumber == computerNumber:
#         print("You got it right on the first guess")
#         break
#     else:
#         if guessedNumber < computerNumber:
#             print("Please guess higher")
#         else:
#             print("Please guess lower")
#         guessedNumber = int(input())
#         if guessedNumber == computerNumber:
#             print("Welldone, you have guessed correctly")
#             break
#     gameCount += 1
#     if gameCount == 3:
#         print("GAME OVER......play again")
#         break


