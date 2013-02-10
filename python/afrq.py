import math

__author__ = 'ekarpov'

a = [float(x) for x in input().split()]
b = []
for aa in a:
    q = math.sqrt(aa)
    b.append(2 * q - q * q)
print(' '.join(["%.3f" % x for x in b]))