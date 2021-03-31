s = "the quick brown box jumps over the lazy box"

result = {item : s.count(item) for item in s}
print(result)