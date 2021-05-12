s = "Welcome to the word of python programming"

# split
lstwords = s.split()
print(lstwords)

result = []
for item in lstwords:
    result.append((item, len(item)))


print(result)

result1 = [(item, len(item)) for item in lstwords]
print(result1)