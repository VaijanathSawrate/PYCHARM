
def printStudentsDetails(name, age, marks, stream):
    print('Student Details:')
    print("Name: {}, Age: {}, Marks: {}, Stream:{}".format(name, age, marks, stream))



printStudentsDetails('John', 19, 500, 'CSE')

d = {'name':'john', 'stream':'science', 'marks':300, 'age':20}
printStudentsDetails(**d)

#printStudentsDetails(*d)   ## not a correct way for key value pair