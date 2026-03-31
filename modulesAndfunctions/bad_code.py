area = 0


def area_of_square(length: float):
    area = length * length
    return area


# area_of_square(20)
print(f"The area is {area_of_square(30)}")


print("+="*5 + "Better Code" + "+="*5)


def area_of_square_2(length: float) -> float:
    return length * length


area1 = area_of_square_2(35)
print(area1)
