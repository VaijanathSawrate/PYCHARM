fh = open("FileExample.txt")  ## Default mode is read

strContent = fh.read()

fh.close()

print(strContent)

print("Type of strContent", type(strContent))