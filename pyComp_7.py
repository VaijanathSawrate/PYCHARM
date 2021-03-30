s = "Welcome to the world of Python Programming"

lstWords = s.split()
print(lstWords)

# Write a program to generate below output
# [(0, 'Welcome', 7), (1, 'to', 2), (2, 'the', 3), ...]

result = []
for index, item in enumerate(lstWords):
    result.append((index, item, len(item)))


print(result)


result = [(index, item, len(item)) for index, item in enumerate(lstWords)]
print(result)