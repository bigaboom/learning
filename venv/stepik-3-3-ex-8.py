import sys
import re

strings = []

for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        break
    strings.append(line)

pattern = r"\b(\w)(\w)(\w*)\b"

for i in strings:
    if re.search(pattern, i) != -1:
        print(re.sub(pattern, r"\2\1\3", i))
    else:
        print(i)