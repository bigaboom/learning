import sys
import re

strings = []

for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        break
    strings.append(line)

pattern = r"(.*z.{3}z)"
#print(strings)

for s in strings:
    if re.match(pattern, s) != None:
        print(s)