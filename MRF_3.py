nums = list(range(1, 11))
print("Numbers : ", nums)

even = lambda num: num % 2 == 0
print(even)
print("Type of even : ", type(even))

print(even(7))
print(even(10))

result = filter(even, nums)
print("Type of result : ", type(result))
print(result)
#print("List of Even numbers using filter : ",list(result) )
print("Tuple of Even numbers using filter : ",tuple(result) )


# filter gives output as element which satisfies given function paoperty
##====================================================================================


mobject = map(even, nums)

print(mobject)
print("Type of mobject : ", type(mobject))
##print("List of squares of numbers using map : ", list(mobject))
print("Tuple of even  numbers using map : ", tuple(mobject))


###  map gives output as true or false that is that particular satisfies or not function property.

# Filter and Map both gives output only once. Because, once they gives output then they will become empty.