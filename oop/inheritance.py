class Parent:
    hair_color = "brown"
    speaks = ["English"]


class Child(Parent):
    hair_color = "purple"

    def __init__(self):
        super().__init__()
        self.speaks = Parent.speaks + ["German"]


child = Child()
print(child.hair_color)
print(child.speaks)
