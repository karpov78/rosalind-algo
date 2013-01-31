import util

__author__ = 'ekarpov'

s = set()
while True:
    l = input()
    if not l: break
    s.add(l)

s_rc = {util.reverseComplement(x) for x in s}

un = s.union(s_rc)
edges = []
for r in un:
    edges.append((r[:-1], r[1:]))
print('\n'.join([str(x).replace("'", "") for x in sorted(edges)]))