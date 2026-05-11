def fibonaci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = previous + current, current

# fib = fibonaci()
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

def odd_number():
    n = 1
    while True:
        yield n
        n += 2

odd_number = odd_number()
print(next(odd_number))
print(next(odd_number))
print(next(odd_number))
print(next(odd_number))
print(next(odd_number))