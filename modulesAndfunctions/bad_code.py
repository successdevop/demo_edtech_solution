area = 0


def area_of_square(length: float):
    area = length * length
    return area


# area_of_square(20)


def area_of_square_2(length: float) -> float:
    return length * length


if __name__ == "__main__":
    print("+=" * 5 + "Better Code" + "+=" * 5)
    print(f"The area is {area_of_square(30)}")
    area1 = area_of_square_2(35)
    print(area1)
