import sys
import re

strings = []

for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        break
    strings.append(line)

pattern = r"((\w)\2*)"

for i in strings:
    if re.search(pattern, i) != -1:
        print(re.sub(pattern, r"\2", i))
    else:
        print(i)