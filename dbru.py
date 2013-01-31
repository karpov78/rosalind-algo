import util

__author__ = 'ekarpov'

def build_deBruijin_graph(s):
    un = s.union({util.reverseComplement(x) for x in s})
    return [(r[:-1], r[1:]) for r in un]

if __name__ == '__main__':
    s = set()
    while True:
        l = input()
        if not l: break
        s.add(l)
    edges = build_deBruijin_graph(s)
    print('\n'.join([str(x).replace("'", "") for x in sorted(edges)]))