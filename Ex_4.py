try:
    fh = open("ExceptionHandling.txt",'w')
    fh.write("Opening the file.\n")
    fh.write("Enter the number. \n")


    userinput = input("Enter any number :")
    fh.write("User entered number is :" + userinput + "\n")

    result = 100 / int(userinput)
    fh.write("The result is "+ str(result) + "\n")

    print(result)

    # fh.write("Closing the file...\n")
    # fh.close()
except ValueError:
    print("Please enter only numbers.")
except ZeroDivisionError:
    print("Please enter number greater than 0.")
finally:
    fh.write("Closing the file...\n")
    fh.close()