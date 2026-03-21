# import this

word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
text = text.lower()
for char in text:
    if char.isalnum():
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)