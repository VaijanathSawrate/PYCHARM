s = "Welcome to the word of python programming"

# split
lstwords = s.split()
print(lstwords)

result = []
for index, item in enumerate(lstwords):
    result.append((index, item, len(item)))


print(result)

result1 = [(index, item, len(item)) for index, item in enumerate(lstwords)]
