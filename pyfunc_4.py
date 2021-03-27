# Factorial of nnumber

# 5! = 5 * 4!

# n! = n * (n-1)!

def recurFactorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * recurFactorial(num - 1)

n = int(input("Enter any number:"))
out = recurFactorial(n)
print("Factorial of {} is {} ".format(n, out))