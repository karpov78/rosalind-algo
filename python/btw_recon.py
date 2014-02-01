from bisect import bisect_left
from collections import defaultdict

alphabet = '$ACGT'


def indexOf(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError(x)


count_cache = {}


def count(i, l):
    global count_cache
    if i in count_cache:
        return count_cache[i]
    elif i == 0:
        return [0] * len(alphabet)
    else:
        return calc_count(i, l)


def calc_count(i, l):
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
        if j % 100 == 0:
            count_cache[j] = list(c)
    return c


def index(s):
    occ = {}
    res = []
    for i in xrange(len(s)):
        if s[i] in occ:
            j = occ[s[i]] + 1
        else:
            j = 1
        occ[s[i]] = j
        res.append('%s%06d' % (s[i], j))
    return res


class BWT:
    def __init__(self, s):
        self.lf = {}
        self.locate = {}
        self.index = 0
        self.bwt = self.bwt_bucket(s, (i for i in xrange(len(s))), 1)

        i_bwt = index(self.bwt)
        first = sorted([c for c in i_bwt])
        self.lf = {i: indexOf(first, i_bwt[i]) for i in xrange(len(s))}

        self.occ = [-1] * len(alphabet)
        for i in xrange(len(first)):
            sIndex = indexOf(alphabet, first[i][0])
            if self.occ[sIndex] == -1:
                self.occ[sIndex] = i


    def bwt_bucket(self, str, bucket, order):
        d = defaultdict(list)
        for i in bucket:
            key = str[i:i + order]
            d[key].append(i)
        result = ''
        for key, v in sorted(d.iteritems()):
            if len(v) > 1:
                result += self.bwt_bucket(str, v, order * 2)
            else:
                result += str[v[0] - 1]
                #                if self.index % 10 == 0:
                self.locate[self.index] = v[0]
                self.index += 1
        return result

    def bwmatch(self, p):
        top = 0
        bottom = len(self.bwt) - 1
        while top <= bottom:
            if len(p) > 0:
                s = p[-1]
                p = p[:-1]
                sIndex = indexOf(alphabet, s)
                top = self.occ[sIndex] + count(top, self.bwt)[sIndex]
                bottom = self.occ[sIndex] + count(bottom + 1, self.bwt)[sIndex] - 1
            else:
                return [self.locate_position(idx) for idx in xrange(top, bottom + 1)]
                # return bottom - top + 1
        return []

    def locate_position(self, idx):
        index_offset = 0;
        while not idx in self.locate:
            if self.bwt[idx] == '$':
                return -1 * index_offset
            index_offset -= 1
            idx = self.lf[idx]
        return self.locate[idx] + index_offset

    def __str__(self):
        return 'BWT: %s\nLocate: %s\nLF: %s' % (self.bwt, self.locate, self.lf)


s = raw_input() + '$'
patterns = raw_input().split(' ')
d = int(raw_input())

b = BWT(s)

for p in patterns:
    seeds = [p[i:i + d + 1] for i in xrange(len(p) - d)]
    print seeds

# res = []
# while True:
#     p = raw_input()
#     if not p: break
#     res += b.bwmatch(p)
# res.sort()
# print ' '.join([str(x) for x in res])

# with open('/Users/evgeny/Downloads/patternMatch.txt', 'r') as f:
#     f.readline()
#     s = f.readline().strip() + '$'
#     b = BWT(s)
#     print 'BWT done'
#
#     res = []
#     while True:
#         p = f.readline().strip()
#         if p == 'Output:':
#             break
#         m = b.bwmatch(p)
#         for x in m:
#             assert s[x:x + len(p)] == p, "Invalid match for %s (%d reported), but was %s" % (p, x, s[x:x + len(p)])
#         res += m
#     res.sort()
#
#     exp = [int(x) for x in f.readline().strip().split(' ')]
#     assert exp == res, "Expected \n%s\n, but was \n%s" % (str(exp), str(res))
