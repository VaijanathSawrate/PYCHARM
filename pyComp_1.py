# Approach 1

result = []

for item in range(1, 11):
    result.append(item * item)


print(result)


# Approach 2

result = [item * item for item in range(1, 11)]

print(result)


## We can also write in single line also
print([item * item for item in range(1, 11)])