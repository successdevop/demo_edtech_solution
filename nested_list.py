empty_list = []
even = [2,4,6,8]
odd = [1,3,5,7,9]
number = [even, odd]

print(number)
for numerList in number:
    print(numerList)
    for i in numerList:
        print(i)
