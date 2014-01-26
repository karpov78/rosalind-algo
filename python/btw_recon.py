from bisect import bisect_left


def indexOf(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError(x)


count_cache = {}


def count(i, l, alphabet='$ACGT'):
    global count_cache
    if i in count_cache:
        return count_cache[i]
    elif i == 0:
        return [0] * len(alphabet)
    else:
        c = list(calc_count(i - 1, l, alphabet))
        c[indexOf(alphabet, l[i - 1][0])] += 1
        count_cache[i] = c
        return c


def calc_count(i, l, alphabet='$ACGT'):
    global count_cache
    c = [0] * len(alphabet)
    start = 0
    for start in xrange(i, -1, -1):
        if start in count_cache:
            c = list(count_cache[start])
            break
    for j in xrange(start + 1, i + 1):
        sIndex = indexOf(alphabet, l[j - 1][0])
        c[sIndex] += 1
        count_cache[j] = list(c)
    return c


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


def bwmatch(firstOccurrence, l, p, alphabet='$ACGT'):
    top = 0
    bottom = len(l) - 1
    while top <= bottom:
        if len(p) > 0:
            s = p[-1]
            p = p[:-1]
            sIndex = indexOf(alphabet, s)
            top = firstOccurrence[sIndex] + count(top, l, alphabet)[sIndex]
            bottom = firstOccurrence[sIndex] + count(bottom + 1, l, alphabet)[sIndex] - 1
        else:
            return bottom - top + 1
    return 0

s = raw_input()
p = raw_input().split(' ')
# with open('/Users/evgeny/Downloads/bwtMatch.txt') as f:
#     f.readline()
#     s = f.readline().strip()
#     p = f.readline().strip().split(' ')
#     f.readline()
#     exp = [int(x) for x in f.readline().strip().split(' ')]

alphabet = '$ACGT'
f = [c for c in s]
f.sort()
firstOccurrence = [-1] * len(alphabet)
for i in xrange(len(f)):
    sIndex = indexOf(alphabet, f[i])
    if firstOccurrence[sIndex] == -1:
        firstOccurrence[sIndex] = i
l = [c for c in s]

res = [bwmatch(firstOccurrence, l, x, alphabet) for x in p]
print ' '.join([str(x) for x in res])
# assert exp == res, "Expected \n%s\n, but was \n%s" % (str(exp), str(res))
