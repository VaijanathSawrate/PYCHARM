result = (item * item for item in range(10000000))
print(result)

# Generators
# Yields

for item in result:
    print(item)