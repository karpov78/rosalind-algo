from python.ctbl import createCharTable, parseTree

MODULO = 1000000

def profile(row, node):
    z = sum([1 if c == '0' else 0 for c in row])
    o = sum([1 if c == '1' else 0 for c in row])
    if row[node] == '0':
        z -= 1
    else:
        o -= 1
    return z, o


def weight(row, node):
    c = profile(row, node)
    return c[0] - c[1]


def c2n(n):
    return n * (n - 1) / 2


def calcQuartets(row):
    z = sum([1 if c == '0' else 0 for c in row])
    o = len(row) - z

    cz = z * (z - 1) / 2
    co = o * (o - 1) / 2
    return cz * co

if __name__ == '__main__':
    n = int(input())
    s = input()
    tree = parseTree(s)
    charTable = [list(x) for x in createCharTable(tree)]
    print('\n'.join([''.join(x) for x in charTable]))
    print('==================================================')

    res = 0

    single_nodes = set()
    idx = 0
    while idx < n:
        charTable.sort(key=lambda x: weight(x, idx))
        prev = None
        clearRow = None
        for i in range(len(charTable)):
            r = charTable[i]
            curr = profile(r, idx)
            if not prev is None and prev == (curr[0] - curr[1]):
                cmp = 0
                for j in range(len(r)):
                    if j != idx and r[j] == charTable[i - 1][j]:
                        cmp += 1
                if cmp == 0 or cmp == len(r) - 1:
                    res = curr[0] * c2n(curr[1]) + curr[1] * c2n(curr[0])
                    if res > MODULO:
                        res %= MODULO
                    single_nodes.add(idx)
                    break
            prev = curr[0] - curr[1]
        idx += 1

    print('\n'.join([''.join(x) for x in charTable]))
    print('--------------------------------')

    k = len(charTable) # number of couples
    s = n - 2 * k - len(single_nodes) # singles left
    #res += s * (nodes - 1) * (nodes - 2) * (nodes - 3) / 6
    if res > MODULO:
        res %= MODULO
    res += k * k * (2 * k - 2)
    if res > MODULO:
        res %= MODULO

    print(res)
