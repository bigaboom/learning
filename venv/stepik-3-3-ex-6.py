import sys
import re

strings = []

for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        break
    strings.append(line)

pattern = r"(human)"

for i in strings:
    if re.search(i, "computer") != -1:
        print(re.sub(pattern, "computer", i))
    else:
        print(i)