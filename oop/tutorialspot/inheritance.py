class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def divide(self):
        return self.a / self.b


class Modulus:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mod_divide(self):
        return self.a % self.b


class DivMod(Division, Modulus):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.a = a
        self.b = b

    def div_and_mod(self):
        div_val = Division.divide(self)
        mod_val = Modulus.mod_divide(self)
        return div_val, mod_val

#
# div = Division(5,6)
# mod = Modulus(10, 3)

# div_mod = DivMod(14, 4)
#
# print("Division: ", div_mod.divide())
# print("Modulus: ", div_mod.mod_divide())
# print("DivMod: ", div_mod.div_and_mod())
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")
        super().show()

class C(A):
    def show(self):
        print("Class C")
        super().show()

class D(B, C):
    # def show(self):
    #     print("Class D")
    #     super().show()
    pass
#
# d = D()
# d.show()


class Student:

    def __init__(self, name="Rajaram", marks=50):
        self.__name = name
        self.__marks = marks

    def studentdata(self):
        print("Name: {} marks: {}".format(self.__name, self.__marks))


s1 = Student()
s2 = Student("Bharat", 25)

s1.studentdata()
s2.studentdata()
print("Name: {} marks: {}".format(s1.__name, s2.__marks))
print("Name: {} marks: {}".format(s2.__name, __s2.marks))