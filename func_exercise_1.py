def sum_eo(n, t):
    if t not in ("e", "o"):
        return -1

    total = 0
    for i in range(n):
        if (t == "e" and i % 2 == 0) or (t == "o" and i % 2 != 0):
            total += i

    return total


print(sum_eo(7, "o"))
