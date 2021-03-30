websites = ['amazon', 'flipcart', 'paytm']

# Using List Comprehensions create the following lists

# list = ['www.amazon.com', www.flipcart.com, www.paytm.com]

result = ["www." + item + "." + "com" for item in websites]
print(result)