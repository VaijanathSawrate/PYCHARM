# Packing and Unpacking

def multipleUnpacking(*args):
    print("Args:", args)
    print("Type of Args:", type(args))


l1 = [10, 20, 30]
multipleUnpacking(*l1)

t1 = (11, 12, 13)
multipleUnpacking(*t1)

s1 = {100, 200, 300}
multipleUnpacking(*s1)

d1 = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
multipleUnpacking(*d1)                   ## for dictionary it wiil only takes key values

r = range(2, 7)
multipleUnpacking(*r)

print(*range(3, 6), sep='')       # it will separate the values of range by no space.
print(*range(2, 9), sep='\n')     # It will separate the values of range by new line.
                             ## PYTHON 3.5  ==> THIS ARGUMENT IS AVAILABLE ONLY FROM 3.5

def multipleUnpacling1(**kwargs):           # For keyword arguments
    print("Kwargs:", kwargs)
    print("Type of Kwargs:", type(kwargs))


multipleUnpacling1(**d1)


#multipleUnpacking(**d1)

