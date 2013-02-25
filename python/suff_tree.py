import sys

from python.timer import Timer


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
            res += '\n' + c.printEdge(tree, '\t' + indent)
        return res

    def getValue(self, tree):
        return tree.s[self.offset, self.length]

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

    def add(self, offset, length):
        for e in self.edges:
            if e.offset == offset:
                return e
        self.edges.append(Edge(Node(), offset, length))
        return self.edges[-1]

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

    def __str__(self):
        return ' '.join([str(x) for x in self.edges])


class SuffixTree:
    def __init__(self, s=None, progress=False):
        self.s = s
        self.root = Node()
        if s:
            l = len(s)
            for k in range(1, l):
                if progress and k % 10 == 1:
                    sys.stdout.write("%.3f%%\r" % (k * 100 / l))
                    sys.stdout.flush()
                self.append(s, offset=l - k, s_len=l)
            if progress:
                sys.stdout.write("100%\r")
                sys.stdout.flush()
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

    def __str__(self):
        return '\n'.join([x.printEdge(self) for x in self.root.edges])

if __name__ == '__main__':
    s = input()
    timer = Timer()
    with (timer):
        print(SuffixTree(s, progress=True))
    print(timer)