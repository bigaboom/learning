import sys
import re

strings = []

for line in sys.stdin:
    line = line.rstrip()
    if line == '':
        break
    strings.append(line)
    # process line

#print(strings)
pattern = r".*(cat).*(cat)"

for i in strings:
    if re.match(pattern, i) != None:
        print(i)