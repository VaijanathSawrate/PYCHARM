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

def sortKeyEmployeeName(emp):
    return emp.name

def sortKeyEmployeeAge(emp):
    return emp.age

def sortKeyEmployeeSalary(emp):
    return emp.salary

sortedlist = sorted(lstemp, key=sortKeyEmployeeName)
print("Sprted list of Employees (Name)            :",sortedlist)

sortedlist = sorted(lstemp, key=sortKeyEmployeeAge)
print("Sprted list of Employees (Age)             :",sortedlist)

sortedlist = sorted(lstemp, key=sortKeyEmployeeSalary)
print("Sprted list of Employees (Salary)          :",sortedlist)

print("Reverse Sorting  :")

sortedlist = sorted(lstemp, key=sortKeyEmployeeName, reverse=True)
print("Sprted list of Employees (Name)            :",sortedlist)

sortedlist = sorted(lstemp, key=sortKeyEmployeeAge, reverse=True)
print("Sprted list of Employees (Age)             :",sortedlist)

sortedlist = sorted(lstemp, key=sortKeyEmployeeSalary, reverse=True)
print("Sprted list of Employees (Salary)          :",sortedlist)

print("IN-PLACE SORTING")
lstemp.sort(key=sortKeyEmployeeName)
print("Sprted list of Employees (Name)            :",lstemp)

lstemp.sort(key=sortKeyEmployeeAge)
print("Sprted list of Employees (Age)             :",lstemp)

lstemp.sort(key=sortKeyEmployeeSalary)
print("Sprted list of Employees (Salary)          :",lstemp)

print("-------------------------------------------------------------------------------")
print("IN-PLACE LAMBDA SORTING")

lstemp.sort(key=lambda emp: emp.name)
print("Sprted list of Employees (Name)            :",lstemp)

lstemp.sort(key=lambda emp: emp.age)
print("Sprted list of Employees (Age)             :",lstemp)

lstemp.sort(key=lambda emp: emp.salary)
print("Sprted list of Employees (Salary)          :",lstemp)

