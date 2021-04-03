import numberword


print("__name__value for this file: ", __name__)
print("__name__ value for numberword: ", numberword.__name__)

userInput = input("Enter any number:")
numberword.printNumberToWords((int(userInput)))