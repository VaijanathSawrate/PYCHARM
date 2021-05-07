### Iterfactorial of a number.

# 0! = 1
# 1! = 1

#n = n * (n - 1)!

def recurfactorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * recurfactorial(num - 1)


num = int(input("Enter any nymber: "))
out = recurfactorial(num)
#print(out)
print("Factorial of {} is {}".format(num, out))
