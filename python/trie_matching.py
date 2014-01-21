from suff_tree import SuffixTree

bitmap = {'A': 0, 'C': 1, 'G': 2, 'T': 3, '$': 4}


class EndNode:
    def __init__(self, l):
        self.suffix_len = l


class Node:
    def __init__(self, s, e=None):
        self.edges = [None] * 5
        self.nodes = [Node] * 5
        idx = bitmap[s[0]]
        self.edges[idx] = s
        self.nodes[idx] = EndNode(len(s)) if not e else e

    def add(self, s, l=None):
        if not l: l = len(s)

        idx = bitmap[s[0]]
        if not self.edges[idx]:
            self.edges[idx] = s
            self.nodes[idx] = EndNode(l)
            return
        edge = self.edges[idx]
        for i in xrange(min(len(s), len(edge))):
            if s[i] != edge[i]:
                part1 = edge[:i]
                part2 = edge[i:]
                self.edges[idx] = part1
                node1 = self.nodes[idx]
                self.nodes[idx] = Node(part2, node1)
                self.nodes[idx].add(s[i:], l)
                return


def populateTrie(root, s):
    node = root
    i = 0
    for c in s:
        idx = bitmap[c]
        if not node[idx]:
            node[idx] = ''
        node = node[idx]


def depth(n):
    res = []
    for e in n:
        if e:
            res += [d + 1 for d in depth(e)]
    if len(res) == 0:
        return [0]
    return res


def find(tree, s, node=None, depth=0):
    r = tree.root if not node else node
    for e in r.edges:
        i = 0
        while len(s) > i and e.length > i and tree.s[e.offset + i] == s[i]:
            i += 1
        if len(s) == i:
            return [len(tree.s) - depth - e.length - x for x in e.end.positions()]
        if e.length == i:
            return find(tree, s[i:], e.end, depth + e.length)
    return []


t = raw_input()
st = SuffixTree(t + '$')
#print st

res = []
while True:
    s = raw_input()
    if not s:
        break

    r = find(st, s)
    res += r
    print r
print ' '.join([str(x) for x in sorted(res)])
