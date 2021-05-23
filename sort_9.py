from operator import attrgetter
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


    def __repr__(self):
        return '{}-{}-{}'.format(self.name, self.age, self.salary)



e1 = Employee('ABC', 25, 7000)
e2 = Employee('XYZ', 55, 700)
e3 = Employee('DEF', 65, 70)

lstemp = [e1, e2, e3]
print("List of Employees      :", lstemp)

sortedlist = sorted(lstemp, key=attrgetter('name'))
print("Sprted list of Employees (Name)            :",sortedlist)

sortedlist = sorted(lstemp, key=attrgetter('age'))
print("Sprted list of Employees (Name)            :",sortedlist)

sortedlist = sorted(lstemp, key=attrgetter('salary'))
print("Sprted list of Employees (Name)            :",sortedlist)