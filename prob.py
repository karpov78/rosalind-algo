import math

__author__ = 'ekarpov'

s = input()
data = [float(s) for s in input().split(' ')]

res = []
for d in data:
    p = {'A': (1 - d) / 2, 'T': (1 - d) / 2, 'C': d / 2, 'G': d / 2}

    P = float(1)
    for c in s:
        P *= p[c]

    res.append(math.log(P, 10))

print(' '.join(["%.3f" % x for x in res]))