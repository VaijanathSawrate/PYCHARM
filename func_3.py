### Iterfactorial of a number.

# 0! = 1
# 1! = 1

def iterfactorial(num):
    result = 1
    for item in range(1, num + 1):
        result = result * item
    return result


num = int(input("Enter any nymber: "))
out = iterfactorial(num)
#print(out)
print("Factorial of {} is {}".format(num, out))


## Sum of firt n numbers
def sum_of_1st_n_numbers(num):
    result = 0
    for item in range(num + 1):
        result = result + item
    return result



out1 = sum_of_1st_n_numbers(num)
#print(out1)
print("Addition of first {} numbers is {}".format(num, out1))