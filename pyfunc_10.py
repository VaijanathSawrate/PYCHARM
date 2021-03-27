# kwargs ==> Dictionnary


def printstudentdetails(**kwargs):
    print("kwargs: ", kwargs)
    print("Type(kwargs: ", type(kwargs))
    print("id(kwargs): ", id(kwargs))
    print("StudentDetails:  Name: {}, Age: {}, Marks: {}, Stream: {}"
          .format(kwargs['name'], kwargs['age'], kwargs['marks'], kwargs['stream']))


# printstudentdetails(name='Mary', age=15, marks=500, stream='CSE')


d = {"name": "Vijay", "Stream": "Fm", "Age": 30, "Marks": 300}
print("id(d): ", id(d))
printstudentdetails(**d)