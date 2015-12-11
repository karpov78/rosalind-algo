def maj(_a):
    res = -1
    depth = 1
    for i in _a:
        if res != i:
            depth -= 1
            if depth == 0:
                res = i
                depth = 1
        else:
            depth += 1
    count = 0
    for i in _a:
        if i == res:
            count += 1
    if count > len(_a) // 2:
        return res
    return -1

if __name__ == '__main__':
    with open('/Users/evgeny/Downloads/rosalind_maj.txt') as f:
        k, n = (int(x) for x in f.readline().split())
        res = []
        for i in xrange(k):
            res.append(maj([int(x) for x in f.readline().split()]))
    print ' '.join((str(x) for x in res))