class Employee:
    def __init__(self, firstname, lastname, age, salary):
        self.fn = firstname
        self.ln = lastname
        self.age = age
        self.salary = salary
        self.email = self.fn + "." +self.ln + "@gmail.com"

    def printDetails(self):
        print("Employee Details  :")
        print("Firstname : {}, Lastname : {}, Age : {}, Salary : {}, Email : {}".format(
            self.fn, self.ln, self.age, self.salary, self.email
        ))


# Inherited / Derived / Subclass / Child
class Developer(Employee):
    pass

class Manager(Employee):
    pass


e1 = Developer("Virat", "Kohli", 32, 5000)
e1.printDetails()

e2 = Manager("MS", "Dhoni", 37, 7000)
e2.printDetails()
