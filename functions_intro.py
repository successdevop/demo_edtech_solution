# def multiply():
#     result = 10.5 * 4
#     return result
#
# answer = multiply()
# print(answer)

# def multiply(x, y):
#     result = x * y
#     return result
#
# for i in range(1, 10):
#     two_times = multiply(2, i)
#     print(two_times)

def is_palindrome(string):
    string = string.lower()
    backwards = string[::-1]
    return backwards == string
#
#
# word = input("Please enter your word here: ")
# if is_palindrome(word):
#     print("'{}' is palindrome".format(word))
# else:
#     print("'{}' is not palindrome".format(word))


def palindrome_sentence(sentence):
    new_word = ""
    for word in sentence:
        if word.isalnum():
            new_word += word
    return is_palindrome(new_word)
    # return new_word[::-1].casefold() == new_word.casefold()


print(palindrome_sentence("Was it a car, or a cat, I saw"))





