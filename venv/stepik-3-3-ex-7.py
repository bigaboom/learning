import sys
import re

strings = []

for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        break
    strings.append(line)

pattern = r"\b[Aa]{1,}\b"

for i in strings:
    if re.search(pattern, i) != -1:
        print(re.sub(pattern, "argh", i, count=1))
    else:
        print(i)