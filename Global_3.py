runscore = 1

def localfunction():
    runscore = 2  ##Create a new local objects
    print("The value of runscore in LocalFunction is:", runscore)



def GlobalFunction():
    global runscore
    runscore = 3
    print("The value of runscore in GlobalFunction is:", runscore )



print(runscore)

localfunction()
print("After calling LocalFunction, The value of runscore in main:",runscore)

GlobalFunction()
print("After calling GlobalFunction, The value of runscore in main:",runscore)

