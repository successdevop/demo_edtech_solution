def factorial(n: int) -> int:
    """
    this function takes an int value and returns it factorial.
    factorial is a multiplication of all initial numbers before a
    particular number but with the inclusion of the number itself
    """
    if n == 0:
        return 1

    output = 1

    for i in range(1, n+1):
        output *= i

    return output


for val in range(36):
    print(val, factorial(val))
