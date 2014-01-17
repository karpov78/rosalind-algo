p = raw_input()
perm = [int(x) for x in p[1:-1].split(' ')]

bp = 1
for i in xrange(len(perm) - 1):
    if perm[i] + 1 != perm[i + 1]:
        bp += 1
print bp