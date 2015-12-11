def degree(g, u):
    res = [0] * u
    for n1, n2 in g:
        res[n1 - 1] += 1
        res[n2 - 1] += 1
    return res

if __name__ == '__main__':
    with open('/Users/evgeny/Downloads/rosalind_deg.txt') as f:
        u, v = (int(x) for x in f.readline().split())
        g = []
        while True:
            line = f.readline()
            if not line:
                break
            g.append((int(x) for x in line.split()))
    result = degree(g, u)
    print ' '.join([str(x) for x in result])