class Person:
    def __init__(self, fname: str, lname: str):
        self.__first_name = fname
        self.last_name = lname

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, name):
        if len(name) >= 3:
            self.__first_name = name
        else:
            print("Name character must be atleast three(3)")

    def printname(self):
        print(self.__first_name, self.last_name)


class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.__grade = 0
        self.graduation = year

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")

    def get_status(self):
        if self.__grade >= 50:
            return "Passed"
        else:
            return "Failed"

    def welcome(self):
        print("Welcome", self.last_name, self.get_first_name(), "to the class of ", self.graduation)


s1 = Student("Success", "Raphael", 2017)
s1.printname()
print(s1.graduation)
s1.welcome()
s1.set_first_name("Doe")
print(s1.get_first_name())
print(s1.get_grade())
print(s1.get_status())
s1.set_grade(49)
print(s1.get_status())
s1.set_grade(50)
print(s1.get_status())
