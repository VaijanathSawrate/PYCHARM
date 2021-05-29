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


e1 = Employee("Virat", "Kohli", 32, 5000)
e1.printDetails()
print("e1 Details  :", e1.__dict__)
