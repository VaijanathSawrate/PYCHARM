def MultipleUnpackings(*args):
    print("Args: ",args)
    print("Type(args: ", type(args))


a = [1, 2 , 3]
MultipleUnpackings(*a)

b = (4, 5, 6)
MultipleUnpackings(*b)

r = range(100, 105)
MultipleUnpackings(*r)

print(*range(1, 6), sep='')      # PYTHON 3.5 ==> This feature is available only from python 3.5