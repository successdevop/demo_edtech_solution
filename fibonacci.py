def fibonacci(n: int) -> int:
    if 0 <= n <= 1:
        return n

    numbers = [0, 1]

    for i in range(n - 1):
        index_addition = numbers[i] + numbers[i+1]
        numbers.append(index_addition)

    print(numbers)
    return numbers[-1]


print(fibonacci(35))


def fibonacci_2(n: int) -> int:
    if 0 <= n <= 1:
        return n

    result = None
    num_1, num_2 = 1, 0
    for i in range(n-1):
        result = num_1 + num_2
        num_2 = num_1
        num_1 = result
    return result


print(fibonacci_2(35))