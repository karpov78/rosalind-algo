def binary_search(ss, start=None, finish=None):
    global s, sa, len_s

    len_sa = len(sa)
    if not start: start = 0
    if not finish: finish = len_sa

    if len_sa == 0: return 0

    while start < finish:
        x = (start + finish) / 2
        off_1 = sa[x]
        hit = False
        for i in xrange(len_s - off_1):
            if s[off_1 + i] > ss[i]:
                finish = x
                hit = True
                break
            elif s[off_1 + i] < ss[i]:
                start = x + 1
                hit = True
                break
        if not hit:
            return x + 1
    return start


s = raw_input()
len_s = len(s)

sa = []
for i in xrange(len_s - 1, -1, -1):
    ss = s[i:]
    sa_idx = binary_search(ss)
    sa.insert(sa_idx, i)

with open('/Users/evgeny/Downloads/result.txt', 'w') as f:
    f.write(', '.join([str(x) for x in sa]))