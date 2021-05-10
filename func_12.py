def emptyListAsParam(my_list = []):
    my_list.append('$')
    return my_list


r = emptyListAsParam()
print('Returned output of 1st Iteration:', r)

r1 = emptyListAsParam()
print('Returned output of 2nd Iteration:', r1)

r3 = emptyListAsParam()
print('Returned output of 3rd Iteration:', r3)

r4 = emptyListAsParam([1, 2, 3])
print('Returned output of 4th Iteration:', r4)   ## This behaviour is not good of empty list