def prob(s, gc):
    P = {'A': (1 - gc) / 2, 'T': (1 - gc) / 2, 'C': gc / 2, 'G': gc / 2}
    p = 1
    for c in s:
        p *= P[c]
    return p


n = int(input())
s = input()

A = [float(x) for x in input().split(' ')]

res = []
for a in A:
    res.append(prob(s, a) * (n - len(s) + 1))

print(' '.join(['%.4f' % x for x in res]))