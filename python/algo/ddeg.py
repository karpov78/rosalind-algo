def degree(_g, _u):
    res = [0] * _u
    for n1, n2 in _g:
        res[n1 - 1] += 1
        res[n2 - 1] += 1
    return res


def double_degree(_deg, _g, _u):
    res = [0] * _u
    for n1, n2 in _g:
        res[n1 - 1] += _deg[n2 - 1]
        res[n2 - 1] += _deg[n1 - 1]
    return res


if __name__ == '__main__':
    with open('/Users/evgeny/Downloads/rosalind_ddeg.txt') as f:
        u, v = (int(x) for x in f.readline().split())
        g = []
        while True:
            line = f.readline()
            if not line:
                break
            g.append([int(x) for x in line.split()])
    deg = degree(g, u)
    print ' '.join([str(x) for x in double_degree(deg, g, u)])
