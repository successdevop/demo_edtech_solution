class Person:
    def __init__(self, fname: str, lname: str):
        self.__first_name = fname
        self.last_name = lname

    def get_first_name(self):
        return self.__first_name

    def printname(self):
        print(self.__first_name, self.last_name)


class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.graduation = year

    def welcome(self):
        print("Welcome", self.last_name, self.get_first_name(), "to the class of ", self.graduation)


s1 = Student("Success", "Raphael", 2017)
s1.printname()
print(s1.graduation)
s1.welcome()