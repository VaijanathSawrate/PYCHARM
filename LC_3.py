## Given a subject  = ''MATHEMATICS , print all the constraints in a list
## ['M', 'T', 'H', 'M', 'T', 'C', 'S']
## Approach 1
result = []
for item in 'MATHEMATICS':
    if item not in 'AEIOU':
        result.append(item)
print(result)

## Approach List Comprehensions

result1 = [item for item in 'MATHEMATICS' if item not in 'AEIOU']
print(result1)