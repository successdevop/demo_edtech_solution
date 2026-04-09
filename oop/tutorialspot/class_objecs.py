class Employee:
    empCount = 0

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @classmethod
    def show_count(cls):
        print(f"Total Employee: {cls.empCount}")

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary:,}"


emp1 = Employee("Success", 1_000_000)
print(emp1.empCount)
print(emp1)
print()
emp2 = Employee("James", 4_000_000)
print(emp2.empCount)
emp2.show_count()
print(emp2)
Employee.show_count()
print()
emp1.age = 7
emp1.age = 8
del emp1.age
#
# print(getattr(emp1, "salary"))
# print(hasattr(emp2, "age"))
# setattr(emp2, "age", 25)
# print(emp2.age)
# print()
#
# print(Employee.__dict__)
# print(Employee.__doc__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__bases__)

