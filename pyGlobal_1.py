def myfunction():
    a = "LocalValue"
    print(a)
    print("INSIDE myFuncton")


myfunction()
# print(a)    ## Error, the scope of a is within myfunction