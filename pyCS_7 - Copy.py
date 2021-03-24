
## Nested for loop

web=["amazon", "flipcart", "google", "paytm"]

ext=("org", "in", "com")

# www.amazon.org
# www.amazon.in
# www.amazon.com

#for i in web:
 #   for j in ext:
   #     print("www." + i + "." + j)



for i in ext:
    for j in web:
        print("www." + j + "." + i)