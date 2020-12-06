import sys
import os

input = []
f = open(os.path.join(sys.path[0], 'input1.txt'))
for a in f:
    input.append(int(a))
f.close()

answer1 = 0
x = 0

while (answer1 == 0):
    for y in input:
        if input[x] + y == 2020:
            answer1 = input[x] * y
            break
    x = x + 1
print(answer1)

answer2 = 0
x = 0

while (answer2 == 0):
    for y in input:
        for z in input:
            if input[x] + y + z == 2020:
                answer2 = input[x] * y * z
                break
    x = x + 1
print(answer2)