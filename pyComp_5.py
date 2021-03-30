websites = ['amazon', 'flipcart', 'paytm']

extensions = ["com", 'org', 'in']

result = ['www.' + i + "." + j for i in websites for j in extensions]
print(result)


result = []
for i in websites:
    for j in extensions:
        result.append('www.' + i + "." + j)

print(result)