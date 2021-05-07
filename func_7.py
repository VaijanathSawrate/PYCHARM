## Functions As a Parameters

def mysquare(num):
    return num * num


def mycube(num):
    return num * num * num


def WrapperFunction(FnctionAsParam, num):
    return FnctionAsParam(num)


def recurfactorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * recurfactorial(num - 1)


result = WrapperFunction(mysquare, 5)
print("Result: ", result)

## Functions are called first class objects in python
## Clousers
## Decorators

lstfunc = [mysquare, mycube, recurfactorial]

for item in lstfunc:
    print("RESULT: ", item(10))