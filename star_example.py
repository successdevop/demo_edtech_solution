numbers = (1, 2, 3, 4, 5)
# print(numbers)
# print(*numbers)


def test_star(*args: int) -> None:
    print(args)
    for i in args:
        print(i)

#
# test_star(2,4,5,6,8,9,21,11,7)
# test_star()


def func(p1, p2, *args, k, l, **kwargs):
    print("positional-or-keyword:.....{}, {}".format(p1, p2))
    print("var-positional (*args):.....{}".format(args))
    print("keyword:......{}, {}".format(k, l))
    print("var-keyword:.....(**kwargs)....{}".format(kwargs))


# func(23,43, 1, 2, 3, 4, k=34, l=51, k1=7, k2=11, k3=90, k4=34)


def sum_numbers(*args: float) -> float:
    """
    This function takes a var positional arguments of strings
    and returns a summation of them
    """
    output = args
    return sum(output)


print(sum_numbers(1.1, 2, 33))
