websites = ['amazon', 'flipkart', 'paytm']
extensions = ['org', 'com', 'in']

for item in websites:
    for ext in extensions:
        print('www.' + item + '.' + ext)