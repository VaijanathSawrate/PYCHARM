import re

s = "purple alice@google.com abcde helloab@abc.com ---@gmail.com 23@gmail.com"

emails = re.findall(r"[a-z0-9-]+@[a-z]+\.com", s)
print(emails)

