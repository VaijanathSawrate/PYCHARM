def myFunction():
    global temp
    temp = 'Inside myfunction'
    print(temp)


myFunction()
print(temp)     ## NO error bcoz now scope of temp inside as well as outside function