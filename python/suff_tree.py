from timer import Timer


class Edge:
    def __init__(self, e, offset, length):
        self.offset = offset
        self.length = length
        self.end = e

    def split(self, position):
        splitOffset = self.offset + position
        splitLength = self.length - position
        result = self.end.addMoveChildren(splitOffset, splitLength) if splitLength > 0 else self
        self.length = position
        return result

    def printEdge(self, tree, indent=''):
        res = indent + tree.s[self.offset:self.offset + self.length]
        for c in self.end.edges:
            res += '\n' + c.printEdge(tree, '')#'\t' + indent#)
        return res

    def getValue(self, tree):
        return tree.s[self.offset:self.offset + self.length]

    def __str__(self):
        return '%d %d' % (self.offset, self.length)


class Node:
    def __init__(self):
        self.edges = []

    def power(self):
        result = len(self.edges)
        for e in self.edges:
            result += e.end.power()
        return result

    def positions(self):
        if len(self.edges) == 0:
            return [0]
        result = []
        for e in self.edges:
            pos = e.end.positions()
            for p in pos:
                result.append(e.length + p)
        return result

    def add(self, offset, length):
        for e in self.edges:
            if e.offset == offset:
                return e
        self.edges.append(Edge(Node(), offset, length))
        return self.edges[-1]

    def getSuffixLengths(self):
        res = []
        if len(self.edges) > 0:
            for e in self.edges:
                lengths = e.end.getSuffixLengths()
                for l in lengths:
                    res.append(e.length + l)
        else:
            res.append(0)
        return res

    def addMoveChildren(self, offset, length):
        newNode = Node()
        newNode.edges = self.edges
        for e in self.edges: e.s = newNode
        self.edges = [Edge(newNode, offset, length)]
        return self.edges[-1]

    def getAllSuffixes(self, tree):
        res = set()
        for edge in self.edges:
            suffixes = edge.end.getAllSuffixes()
            if len(suffixes) > 0:
                for s in suffixes: res.add(edge.getValue(tree) + s)
            else:
                res.add(edge.getValue(tree))
        return res

    def contains(self, tree, t):
        for e in self.edges:
            if tree.s[e.offset] == t[0]:
                len_t = len(t)
                if len_t <= e.length:
                    return t == tree.s[e.offset: e.offset + len_t]
                else:
                    return e.end.contains(tree, t[e.length:])
        return False


    def __str__(self):
        return ' '.join([str(x) for x in self.edges])


class SuffixTree:
    def __init__(self, s=None):
        self.s = s
        self.root = Node()
        if s:
            l = len(s)
            for k in range(1, l):
                self.append(s, offset=l - k, s_len=l)
            self.append(s)

    def append(self, s, root=None, offset=0, s_len=None):
        if not root: root = self.root
        if not s_len: s_len = len(s)
        for e in root.edges:
            if s[e.offset] == s[offset]:
                r = self.followEdge(e, s, offset, s_len)
                if r:
                    self.append(s, r, offset + e.length, s_len)
                return
        root.add(offset, s_len - offset)

    def followEdge(self, e, s, offset, s_len=None):
        if not s_len: s_len = len(s)
        for i in range(e.length):
            if s[e.offset + i] != s[offset + i]:
                e.split(i)
                e.end.add(offset + i, s_len - offset - i)
                return None
        return e.end

    def getAllSuffixes(self):
        return self.root.getAllSuffixes(self)

    def contains(self, t):
        return self.root.contains(self, t)

    def __str__(self):
        return '\n'.join([x.printEdge(self) for x in self.root.edges])


if __name__ == '__main__':
    s = raw_input()
    timer = Timer()
    with (timer):
        print(SuffixTree(s))
    print(timer)
