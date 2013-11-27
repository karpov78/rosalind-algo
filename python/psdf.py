from python.util import *
from python import matrix

data = []
dna = None
while True:
    line = input()
    if not line:
        break
    if line[0] == '>':
        if dna:
            data.append(dna)
        dna = ''
    else:
        dna += line

res = matrix.Matrix(len(data))

l = None
i = 0
for s in data:
    if not l:
        l = len(s)

    j = 0
    for t in data:
        res[(i, j)] = float(getHammingDistance(s, t)) / l
        j += 1
    i += 1

print(res)