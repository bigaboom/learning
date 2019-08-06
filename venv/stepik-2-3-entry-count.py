s = input()
t = input()
i = 0
k = 0

while s[i::].find(t) != -1:
    i += s[i::].find(t) +1
    k += 1

print(k)