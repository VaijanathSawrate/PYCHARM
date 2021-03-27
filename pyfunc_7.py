# Functions as a PARAMETER
# Function takes function as a parameter

def mysquare(num):
    return num * num


#mysquare(5)

def mycube(n):
    return n * n * n


def iterFactorial(num):
    result = 1
    for item in range(1, num + 1):
        result = result * item

    return result

def WrapperFunction(FunAsParam, num):
    return FunAsParam(num)

result = WrapperFunction(mysquare, 5)
print("Result: ", result)

# Functions are also first class objects in python
# Closures
# Decorators

lstFunc = [mysquare, mycube, iterFactorial]

for item in lstFunc:
    print("Result: ", item(5))