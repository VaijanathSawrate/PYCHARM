import re
s = "Welcome to   Regex   Programming    using    Python"

print("Value of s: ", s)

lstValues = re.split(r"\s", s)
print("Regex split using '\s'       : ", lstValues)

lstValues = re.split(r"\s+", s)
print("Regex split using '\s+'      : ", lstValues)

lstValues = re.split(r"(\s+)", s)
print("Regex split using '(\s+)'    : ", lstValues)

lstValues = re.split(r"s+", s)
print("Regex split using 's+'       : ", lstValues)

lstValues = re.split(r"(s+)", s)
print("Regex split using '(s+)'     : ", lstValues)