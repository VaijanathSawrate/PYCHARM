try:
    userinput = input("Enter any number :")
    result = 100 / int(userinput)
    print(result)
except ValueError:
    print("Please enter only numbers.")
except ZeroDivisionError:
    print("Please enter number greater than 0.")
except:
    print("Please give valid input.")