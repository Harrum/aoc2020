import sys
import os

input = []
f = open(os.path.join(sys.path[0], 'input1.txt'))
for a in f:
    input.append(int(a))
f.close()

for x in input:
    for y in input:
        if x + y == 2020:
            print(x * y)
            break

for x in input:
    for y in input:
        for z in input:
            if x + y + z == 2020:
                print(x * y * z)
                break