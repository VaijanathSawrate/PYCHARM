class Employee:
    __employee_count = 0
    def __init__(self, firstname, lastname, age, salary):
        self.fn = firstname
        self.ln = lastname
        self.age = age
        self.salary = salary
        self.email = self.fn + "." +self.ln + "@gmail.com"
        Employee.__employee_count += 1

    def printDetails(self):
        print("Employee Details  :")
        print("Firstname : {}, Lastname : {}, Age : {}, Salary : {}, Email : {}".format(
            self.fn, self.ln, self.age, self.salary, self.email
        ))

    ## Decorator
    @classmethod
    def GetEmployeeCount(cls):
        return cls.__employee_count

e1 = Employee("Virat", "Kohli", 32, 5000)
e1.printDetails()
print("Employee dict  :", Employee.__dict__)
print("e1 Details  :", e1.__dict__)

e2 = Employee("MS", "Dhoni", 35, 7000)
print("After adding employee dict  :", Employee.__dict__)

# print("Employee count using e1 (object/instance)  :", e1.__employee_count)  ## Error
# print("Employee count using class  :", Employee.__employee_count) ## Error

print("Employee count using class method         :", Employee.GetEmployeeCount())
print("Employee count using instance e1 method   :", e1.GetEmployeeCount())

