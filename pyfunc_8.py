# Args

def SumOfNumbers(*args):
    print("Args: ", args )
    print("Tpye(args): ", type(args))
    result = 1
    for item in args:
        result += item
    print("Result: ", result)


SumOfNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#SumOfNumbers(3, 5)
