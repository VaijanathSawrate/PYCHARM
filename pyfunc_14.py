def EmptyListAsParam(my_list=None):
    if my_list is None:
        my_list=[]
    my_list.append("$")
    return my_list


r = EmptyListAsParam()
print("Returned output 1st Iteration: ", r)

r1 = EmptyListAsParam()
print("Returned output 2nd Iteration: ", r1)

r2 = EmptyListAsParam()
print("Returned output 3rd Iteration: ", r2)

r3 = EmptyListAsParam([1,2,3])
print("Returned output 3rd Iteration: ", r3)