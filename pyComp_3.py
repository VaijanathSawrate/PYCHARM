# Given the subject = "MATHEMATICS" print all consonents in the list
# ['M', 'T', 'H', 'M', 'T', 'C', 'S']

str = 'MATHEMATICS'
str1 = 'AEIOU'
result = []

for item in str:
    if item not in str1:
        result.append(item)


print(result)

print([item for item in "MATHEMATICS" if item not in "AEIOU"])