from operator import itemgetter

lstemp = [('ABC', 25, 7000), ('XYZ', 55, 700), ('DEF', 65, 70)]

print("Original list       :", lstemp)

sortedlist = sorted(lstemp, key=itemgetter(0))
print("Sprted list of Employees (Name)            :",sortedlist)

sortedlist = sorted(lstemp, key=itemgetter(1))
print("Sprted list of Employees (Name)            :",sortedlist)

sortedlist = sorted(lstemp, key=itemgetter(2))
print("Sprted list of Employees (Name)            :",sortedlist)
