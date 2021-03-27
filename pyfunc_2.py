# Write a function to find maximum of two number

def findMaximum(x, y):
    if x > y:
        return x
    else:
        return y

result = findMaximum(3, 5)
print(result)