from functools import reduce

nums = list(range(1, 11))
print(nums)


AddNos = lambda x, y: x + y
print( "Addition of two numbers : ", AddNos(12, 23))


result = reduce(AddNos, nums)
print("Result : ", result)


Mult = lambda x, y: x * y
print("Multiplication of two numbers : ", Mult(12, 23))


result = reduce(Mult, nums)  ## It multipy 1st 2 no. then result of multiplication of these two numbers multiply
                                                                           # with 3rd no. and continue this process
print("Result : ", result)
