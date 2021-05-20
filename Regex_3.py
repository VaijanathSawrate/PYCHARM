import re

address = "Hi, 11   89 Main, 4th Cross  123 Road Marathalli 5678 Bangelore  230069 34562."

lstvalues = re.findall(r"\d", address)
print("Regex using \d       :", lstvalues)

lstvalues = re.findall(r"\d+", address)
print("Regex using \d+      :", lstvalues)

lstvalues = re.findall(r"\d{6}", address)
print("Regex using \d{6}    :", lstvalues)

lstvalues = re.findall(r"\d{2}", address)
print("Regex using \d{2}    :", lstvalues)

lstvalues = re.findall(r"\d{1,6}", address)
print("Regex using \d{1,6}  :", lstvalues)

lstvalues = re.findall(r"\s(\d{2})\s", address)
print("Regex using \s\d{2}\s :", lstvalues)