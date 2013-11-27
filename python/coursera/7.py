from util import getHammingDistance, reverseComplement
from timer import Timer


def count(s, p, d):
    len_s = len(s)
    len_p = len(p)

    res = 0
    for x in range(len_s - len_p + 1):
        c = s[x:x + len_p]
        if getHammingDistance(p, c) <= d:
            res += 1
    return res


def dClosure(s, d, fixed=None, res=None):
    fixed = [] if not fixed else fixed
    res = set() if not res else res

    res.add(''.join(s))
    if d == 0:
        return

    for i in range(len(s)):
        if not i in fixed:
            orig = s[i]
            for ch in 'ACGT':
                if ch != orig:
                    s[i] = ch
                    dClosure(s, d - 1, fixed + [i], res)
            s[i] = orig
    return res


if __name__ == '__main__':
    s = [x for x in raw_input()]
    k, d = (int(x) for x in raw_input().split(' '))
    len_s = len(s)

    with Timer() as t:
        dc = {}
        for i in range(len_s - k + 1):
            ss = s[i:i + k]
            closure = dClosure(ss, d)

            rs = [x for x in reverseComplement(''.join(ss))]
            closure.union(dClosure(rs, d))
            for c in closure:
                if c in dc:
                    dc[c] += 1
                else:
                    dc[c] = 1
        print 'd-closure size: %d' % len(dc)

        m_value = 0
        res = []
        for x, f in dc.items():
            rx = reverseComplement(x)
            rf = dc[rx] if rx in dc else 0
            if f + rf > m_value:
                m_value = f + rf
                res = [x]
            elif f + rf == m_value:
                res.append(x)
        print ' '.join(res)
    print t