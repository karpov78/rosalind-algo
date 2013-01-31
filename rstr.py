import math

__author__ = 'ekarpov'

def falseProb(s, gc):
    P = {'A' : (1 - gc) / 2, 'T' : (1 - gc) / 2, 'C' : gc / 2, 'G': gc / 2}
    p = 1
    for c in s:
        p *= P[c]
    return 1 - p

d = input().split(' ')
N = int(d[0])
gc = float(d[1])
s = input()

false_prob = falseProb(s, gc)
print(false_prob)
allFalseProb = float(1)
for i in range(N):
    allFalseProb *= false_prob
print(allFalseProb)
print('%.3f' % (1 - allFalseProb))