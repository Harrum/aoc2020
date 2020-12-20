import sys
import os

f = open(os.path.join(sys.path[0], 'input.txt'))
input = f.readlines()
f.close()

validPasses1 = 0
validPasses2 = 0

for line in input:
    split = line.split(" ")
    min = (int)(split[0].split("-")[0])
    max = (int)(split[0].split("-")[1])
    letter = split[1].replace(":", "")
    password = split[2]

    total = password.count(letter)
    if total >= min and total <= max:
        validPasses1 += 1

    if ((password[min -1] == letter) ^ (password[max - 1] == letter)):
        validPasses2 += 1

print("Valid passes part 1: ", validPasses1)
print("Valid passes part 2: ", validPasses2)