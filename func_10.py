## **Kwargs = Dictionary

def printStudentsDetaila(**kwargs):
    print('Student Details: ')
    print("type(kwargs):", type(kwargs))
    print("id(kwsrgs):", id(kwargs))



d = {'name':'john', 'stream':'science', 'marks':300, 'age':20}
print('id(d):', id(d))
result = printStudentsDetaila(**d)
print(result)
printStudentsDetaila(Name='Harry', age=30, Stream='ECS', Marks=300, Location='Pune')