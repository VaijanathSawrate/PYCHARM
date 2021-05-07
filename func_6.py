## Lambda functions
## Anonymes functions
## Functions which have got no names
## They have used to write one-line functions

def mysquare(num):
    print(num * num)


mysquare(5)

f = lambda num: num * num
print(type(f))
print(f)
print("square of number is ",f(3))

print(" Square of number is",(lambda num: num * num)(10))