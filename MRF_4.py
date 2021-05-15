## Take a sequence of numbers from users
## first number : count
## second to count : all are numbers

## 5 20 34 54 35 65
## 3 77 45 39

userinput = input("")
lstnos = list(map(int, userinput.split()))
print("List of Numbers : ", lstnos)

avg = sum(lstnos[1:]) / lstnos[0]
print(avg)

