import re

sampleString = '''
Rohit made 122 runs, Virat made 96 runs, and
Dhawan made 46 runs and we won the match.
'''

# {"Rohit": 122, "Virat": 96, "Dhawan": 46}

key = re.findall(r"[A-Z][a-z]+", sampleString)
value = re.findall(r"\d{1,3}", sampleString)


print("keys:", key)
print('Values:', value)

lstnames = list(key)
lstRuns = list(value)

result = {lstnames[i]:lstRuns[i] for i in range(3)}
print(result)

result = dict(zip(lstnames, lstRuns))
print(result)

result = {}
for item in range(len(lstnames)):
    result[lstnames[item]] = lstRuns[item]


print(result)