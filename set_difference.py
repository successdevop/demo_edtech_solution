evens = set(range(0, 50, 2))
odd = set(range(1, 50, 2))

print(evens)
print(odd)
print()

primes = {prime if prime % 2 != 0 else 0 for prime in range(100)}
print(primes)
squares = {square ** 2 for square in range(100)}
print(squares)
print()
print(odd.difference(primes))
