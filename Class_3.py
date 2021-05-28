class Employee:
    '''
        Help : An Employee Class Documentation.
        The instance of class can be used to create and manage employee data.
        It stores information like name, age, educational details etc.
        '''
    def __init__(self, firstname, lastname):
        # Similar to constructor
        print("Value of self  :", self)
        self.fn = firstname
        self.ln = lastname


e1 = Employee("Virar", "Kohli")
e2 = Employee("MS", "Dhoni")

print("e1 :", e1)
print("e2 :", e2)

print("e1.dict          :", e1.__dict__)
print("e2.dict          :", e2.__dict__)
print("Employee dict    :", Employee.__dict__)