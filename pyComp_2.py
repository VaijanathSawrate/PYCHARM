# Generate a list of numbers 1 to 20 that are divisible by 3
# Approach 1

result = []

for item in range (1, 20):
    if item % 3 == 0:
        result.append(item)


print(result)


# Approach 2

print([item for item in range(1, 20) if item % 3 == 0])