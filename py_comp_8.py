# Dictionary Comprehensions

# {1 : 1, 2 : 4, 3 : 9, ...}

result = {item : item * item for item in range(1,11)}
print(result)