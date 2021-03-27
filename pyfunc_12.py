def PrintStudentDetails(name, age, marks, stream):
    print("Student Details: ")
    print("Name: {}, Age: {}, Marks: {}, Stream{}".format(
        name, age, marks, stream
    ))



PrintStudentDetails('Mary', 15, 500, 'CSE')
d = {"name": "Vijay", "stream": "Fm", "age": 30, "marks": 300}
PrintStudentDetails(**d)
PrintStudentDetails(*d)  # NOT a correct way
