#pycharam# Find out all words which has at least One Capital alphabet and at least one number
import re

s = "A1bc welcome 2Check paT3ern ano3ter check3aldTe 22Check B5 8C s(p%$Ial5test"

# A N ==> *A*N* *AN* AN* A*N* *N*A* NA *NA* *N*A

# re.search()
lstwords = s.split()
print(lstwords)

for item in lstwords:
    lstPatMatch = re.search(r"(.*[A-Z].*\d.*)|(.*\d.*[A-Z].*)", item)
    if lstPatMatch:
        #print("lstMatched:",lstPatMatch)
        print(lstPatMatch.group(0))