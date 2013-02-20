MODULO = 1000000

def profile(row):
    z = sum([1 if c == '0' else 0 for c in row])
    o = sum([1 if c == '1' else 0 for c in row])
    return z, o


def zeroes(row):
    return profile(row)[0]


def c2n(n):
    return n * (n - 1) // 2


def c4n(n):
    if n > 4:
        return n * (n - 1) * (n - 2) * (n - 3) // 24
    elif n == 4:
        return 1
    else:
        return 0


if __name__ == '__main__':
    n = int(input())
    s = input()
    #    tree = parseTree(s)
    #    charTable = [list(x) for x in createCharTable(tree)]
    #    print('\n'.join([''.join(x) for x in charTable]))
    #    print('==================================================')

    res = 0

    #    x = 0 # of pairs
    #    for r in charTable:
    #        z, o = profile(r)
    #        if z == 2 or o == 2:
    #            x += 1
    #    print("# of pairs = %d" % x)

    q = c4n(n) % MODULO # of all quartets
    print(q)
