import sys
import re

strings = []

for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        break
    strings.append(line)

pattern = r"(.*\bcat\b)"
#print(strings)

for s in strings:
    if re.match(pattern, s) != None:
        print(s)