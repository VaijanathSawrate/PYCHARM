websites = ['amazon', 'flipkart', 'snapdeal', 'paytm']
extensions = ['com', 'in', 'org']

result = ['www.' + item + '.' + ext for item in websites for ext in extensions]
print(result)