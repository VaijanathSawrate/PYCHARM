nums = list(range(1, 11))
print("Numbers : ", nums)

sq = lambda num: num * num

mobject = map(sq, nums)

print(mobject)
print("Type of mobject : ", type(mobject))
##print("List of squares of numbers using map : ", list(mobject))
print("Tuple of squares of numbers using map : ", tuple(mobject))
