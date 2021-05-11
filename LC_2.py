## Generate a list of numbers between 1  to 20 which are divisible by 3.
## Approach 1

result = []
for item in range(1, 21):
    if item % 3 == 0:
        result.append(item)


print(result)

## Approach 2

result = [item for item in range(1, 21) if item % 3 == 0]
print(result)

