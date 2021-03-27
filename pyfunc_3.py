# Factorial of a number
# 5! = 5*4*3*2*1
#0! = 1
# 1! = 1
def iterFactorial(num):
    result = 1
    for item in range(1, num + 1):
        result = result * item

    return result

n = int(input("Enter your number:"))
out = iterFactorial(n)
print("Factorial of {} is {}".format(n, out))