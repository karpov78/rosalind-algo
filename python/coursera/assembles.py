class AdjacencyMatrix:
    def __init__(self, nodes, noEdge=0):
        self.len = len(nodes)
        self.nodes = list(nodes)
        self.node_index = {}
        self.noEdge = noEdge
        for i in xrange(self.len):
            self.node_index[self.nodes[i]] = i
        self.edges = [self.noEdge] * (self.len * self.len)

    def __setitem__(self, key, value):
        if not type(key) is tuple:
            raise Exception('Invalid matrix key')
        elif type(key[0]) is int:
            self.edges[key[0] * self.len + key[1]] = value
        elif type(key[0]) is str:
            s = self.node_index[key[0]]
            e = self.node_index[key[1]]
            self.edges[s * self.len + e] = value

    def __getitem__(self, item):
        if not type(item) is tuple:
            raise Exception('Invalid matrix key')
        elif type(item[0]) is int:
            return self.edges[item[0] * self.len + item[1]]
        elif type(item[0]) is str:
            s = self.node_index[item[0]]
            e = self.node_index[item[1]]
            return self.edges[s * self.len + e]

    def __contains__(self, item):
        if type(item) is str:
            return item in self.node_index
        elif type(item) is int:
            return 0 <= item < self.len
        else:
            raise Exception('Invalid matrix key')

    def assertEquals(self, other):
        assert self.len == other.len
        for i in xrange(self.len * self.len):
            assert other.edges[i] == self.edges[i], 'Invalid entry: expected %s, but was %s' % (
                other.edgeString(i), self.edgeString(i))

    def edgeString(self, index):
        i = index / self.len
        j = index % self.len
        return '%s %s %s' % (self.nodes[i], '->' if self.edges[index] else '  ', self.nodes[j])

    def nodeString(self, i):
        index = i * self.len
        targetNodes = ','.join([self.nodes[j] for j in xrange(self.len) if self.edges[index + j] != self.noEdge])
        if targetNodes:
            return '%s %s %s' % (self.nodes[i], '->', targetNodes)
        else:
            return ''

    def gluedStart(self):
        return [self.nodeString(i) for i in xrange(self.len) if self.nodeString(i)]

    def __str__(self):
        return '\n'.join([self.edgeString(i) for i in xrange(self.len * self.len) if self.edges[i] != self.noEdge])


def Overlap(patterns, k=1):
    len_p = len(patterns)
    res = AdjacencyMatrix(patterns)
    for i in xrange(len_p):
        for j in xrange(len_p):
            if i == j:
                continue
            if patterns[i][k:] == patterns[j][:-k]:
                res[i, j] = 1
    return res


def Composition(text, k):
    res = [text[i: i + k] for i in xrange(len(text) - k + 1)]
    res.sort()
    return res


def DeBruijn(text, k):
    nodes = Composition(text, k - 1)
    res = AdjacencyMatrix(nodes)
    for s in Composition(text, k):
        res[s[:-1], s[1:]] = 1
    return res


if __name__ == '__main__':
    k = int(raw_input())
    text = raw_input()
    print '\n'.join(DeBruijn(text, k).gluedStart())
    # with open('C:\\Users\\ekarpov\\Downloads\\debruijn_graph_string.txt', 'r') as f:
    #     f.readline() # Input:
    #     k = int(f.readline())
    #     text = f.readline().strip()
    #     f.readline() # Output:
    #     expected = []
    #     while True:
    #         s = f.readline().strip()
    #         if not s:
    #             break
    #         expected.append(s)
    #     expected.sort()
    #     db = DeBruijn(text, k).gluedStart()
    #     db.sort()
    #     assert expected == db, 'Expected:\n%s, but was\n%s' % (expected, db)
