websites = ['amazon', 'flipkart', 'paytm']

## Using a list comprehensions generate a below list
## ['www.amazon.com', 'www.flipkart.com', www.paytm.com']


result = ['www.' + item + '.com' for item in websites]
print(result)
