from bisect import bisect_left


def indexOf(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError(x)


def index(s):
    occ = {}
    for i in xrange(len(s)):
        if s[i] in occ:
            j = occ[s[i]] + 1
        else:
            j = 1
        occ[s[i]] = j
        s[i] = '%s%03d' % (s[i], j)
    return s


def bwmatch(f, l, m, p):
    top = 0
    bottom = len(l) - 1
    while top <= bottom:
        if len(p) > 0:
            s = p[-1]
            p = p[:-1]
            newTop = None
            newBottom = None
            for j in xrange(top, bottom + 1):
                if l[j][0] == s and not newTop:
                    newTop = j
                    newBottom = j
                elif l[j][0] == s and newTop:
                    newBottom = j
            if not newTop:
                return 0
            top = last2first[newTop]
            bottom = last2first[newBottom]
        else:
            return newBottom - newTop + 1
    return 0


s = raw_input()
p = raw_input().split(' ')
# with open('/Users/evgeny/Downloads/bwtMatch.txt') as f:
#     f.readline()
#     s = f.readline().strip()
#     p = f.readline().strip().split(' ')
#     f.readline()
#     exp = [int(x) for x in f.readline().strip().split(' ')]

f = [c for c in s]
f.sort()
l = [c for c in s]
index(f)
index(l)
last2first = {i: indexOf(f, l[i]) for i in xrange(len(s))}

res = [bwmatch(f, l, last2first, x) for x in p]
print ' '.join([str(x) for x in res])
# assert exp == res, "Expected \n%s\n, but was \n%s" % (str(exp), str(res))
