alphabets = ['a', 'b', 'c', 'd']

fruits = ['apple', 'banana', 'cherry', 'dates']

# Using the above two lists, create a dictionary using dictionary comprehension

# {'a': ("apple", 5), ...}

result = {alphabets[item] : (fruits[item], len(fruits[item])) for item in range(0, len(fruits))}
print(result)