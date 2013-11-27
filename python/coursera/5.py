CODE = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
R_CODE = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def decode(b, k):
    s = ''
    for i in xrange(0, k):
        s = R_CODE[b & 3] + s
        b >>= 2
    return s


if __name__ == '__main__':
    with open('/Users/evgeny/Downloads/E-coli.txt', 'r+') as f:
        s = f.read()

    #    k, L, t = (int(x) for x in raw_input().split(' '))
    k, L, t = (9, 500, 3)
    len_s = len(s)

    kmers = {}
    b = 0L
    mask = 0
    res = set()
    for i in range(0, k):
        if i > 0:
            b <<= 2
        b += CODE[s[i]]
        mask <<= 2
        mask |= 3

    kmers[b] = [0]
    for i in range(k, len_s):
        b <<= 2
        b += CODE[s[i]]
        b &= mask
        if b in kmers:
            if b in res:
                continue
            entries = kmers[b]
            entries.append(i - k + 1)
            if entries[-1] - entries[0] + k <= L and len(entries) == t:
                res.add(b)
            if entries[-1] - entries[0] + k > L:
                del entries[0]
        else:
            kmers[b] = [i - k + 1]
    print len(res)