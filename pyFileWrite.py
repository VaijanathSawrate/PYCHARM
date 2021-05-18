## w ==> Write mode
## r ==> Read mode
## a ==> Append mode

fh = open('FileExample.txt', 'w')
print("File handle", fh)
print("Type of file", type(fh))

fh.write("Welcome to the file handling in python.\n")
fh.write("This is a second line.\n")
fh.write("Always cose the file, once the work is done.\n")

fh.close()