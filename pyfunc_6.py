# Lambda Functions

# Anonyms Functions
# Functions which got no names
# They are used to write one-lins functions

def mySquare(num):
    return num * num


print(mySquare(7))


f = lambda num: num * num
print(f)
print(type(f))


result = f(3)
print("Square of number: ", (lambda num: num * num)(10))
print("Square of number: ", (lambda num: num * num)(int(input("Enter your number: "))))
