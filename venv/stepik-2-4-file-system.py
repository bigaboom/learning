import os
import os.path

ended = []

for current_dir, dirs, files in os.walk("./main"):
    for i in files:
        if i[-3:] == '.py':
            #print()
            ended.append(current_dir[2:])
            break
ended.sort()
print(ended)
for i in ended:
    print(i)