s = input()
a = input()
b = input()

answer = 'Impossible'
k = 0
while s.find(a) != -1:
    if k == 1000:
        k = -1
        break
    if b.find(a) != -1:
        k = -1
        break
    k += 1
    s = s.replace(a, b)
if k != -1:
    answer = str(k)
print(answer)





