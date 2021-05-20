import re

s = "Welcome   to   Regex    Programming     using      Python"

print("Value of s :", s)

listvalues = re.split(r"\s", s)  ## Whenever you get space split it.
print("Regex split using \s       :", listvalues)

listvalues = re.split(r"\s+", s)   ## Whenever you get one or more spaces consider it as one space and split it.
print("Regex split using \s+      :", listvalues)

listvalues = re.split(r"(\s+)", s)
print("Regex split using (\s+)    :", listvalues)

listvalues = re.split(r"s+", s)
print("Regex split using s+       :", listvalues)

listvalues = re.split(r"(s+)", s)
print("Regex split using (s+)     :", listvalues)

listvalues = re.split(r"(m+)", s)
print("Regex split using (m+)     :", listvalues)

listvalues = re.split(r"s+", s)
print("Regex split using s+       :", listvalues)

listvalues = re.split(r"[a-f]", s)
print("Regex split using [a-f]     :", listvalues)

listvalues = re.split(r"([a-f])", s)
print("Regex split using ([a-f])     :", listvalues)

listvalues = re.split(r"[a-f][l-n]", s)
print("Regex split using [a-f][l-n]    :", listvalues)

listvalues = re.split(r"([a-f][l-n])", s)
print("Regex split using ([a-f][l-n])    :", listvalues)

listvalues = re.split(r"[a-fl-n]", s)
print("Regex split using [a-fl-n]    :", listvalues)

listvalues = re.split(r"[a-f]|[l-n]", s)
print("Regex split using [a-f]|[l-n]    :", listvalues)

listvalues = re.split(r"([a-f]|[l-n])", s)
print("Regex split using ([a-f]|[l-n])    :", listvalues)






