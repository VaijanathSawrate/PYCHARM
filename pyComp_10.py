alphabets = ['a', 'b', 'c', 'd']

fruits = ['apple', 'banana', 'cherry', 'dates']

# Using the above two lists, create a dictionary using dictionary comprehension

# {'a': "apple", ...}

result = {alphabets[item]: fruits[item] for item in range(0, len(alphabets))}
print(result)