import sys

TERMINAL = '*'


class Edge:
    def __init__(self, e, value):
        self.value = value
        self.end = e

    def split(self, position):
        splitValue = self.value[position:]
        result = self.end.addMoveChildren(splitValue) if len(splitValue) > 0 else self
        self.value = self.value[:position]
        return result

    def printEdge(self, indent=''):
        res = indent + self.value
        for c in self.end.edges:
            res += '\n' + c.printEdge('\t' + indent)
        return res

    def __str__(self):
        return self.value


class Node:
    def __init__(self):
        self.edges = []

    def power(self):
        result = len(self.edges)
        for e in self.edges:
            result += e.end.power()
        return result

    def add(self, value):
        for e in self.edges:
            if e.value[0] == value:
                return e
        self.edges.append(Edge(Node(), value))
        return self.edges[-1]

    def addMoveChildren(self, value):
        newNode = Node()
        newNode.edges = self.edges
        for e in self.edges: e.s = newNode
        self.edges = [Edge(newNode, value)]
        return self.edges[-1]

    def getAllSuffixes(self):
        res = set()
        for edge in self.edges:
            suffixes = edge.end.getAllSuffixes()
            if len(suffixes) > 0:
                for s in suffixes: res.add(edge.value + s)
            else:
                res.add(edge.value)
        return res

    def __str__(self):
        return ' '.join([str(x) for x in self.edges])


class Marker:
    def __init__(self, edge):
        self.edge = edge
        self.position = 0

    def next(self, s):
        if len(self.edge.value) > self.position + 1:
            self.position += 1
            return self.edge.value[self.position] == s
        elif len(self.edge.end.edges) == 0:
            self.edge.value += s
            self.position += 1
            return True
        else:
            for sub in self.edge.end.edges:
                if sub.value[0] == s:
                    self.edge = sub
                    self.position = 0
                    return True
            self.position += 1
            return False


class SuffixTree:
    def __init__(self, s=None, progress=False):
        self.root = Node()
        self.markers = []
        if s:
            for k in range(len(s)):
                if progress and k % 10 == 0:
                    sys.stdout.write('\r%.3f%%' % (k * 100 / len(s)))
                    sys.stdout.flush()
                self.append(s[k])

    def append(self, s):
        for m in self.markers:
            if not m.next(s):
                self.split(m, s)

        markerCreated = False
        for e in self.root.edges:
            if e.value[0] == s:
                self.markers.append(Marker(e))
                markerCreated = True
                break
        if not markerCreated:
            self.markers.append(Marker(self.root.add(s)))

    def split(self, marker, s):
        oldEdge = marker.edge
        oldPosition = marker.position
        newEdge = oldEdge.split(oldPosition)
        marker.edge = marker.edge.end.add(s)
        marker.position = 0

        for m in self.markers:
            if m.edge == oldEdge and m.position >= oldPosition:
                m.edge = newEdge
                m.position = m.position - oldPosition

    def getAllSuffixes(self):
        return self.root.getAllSuffixes()

    def __str__(self):
        return '\n'.join([x.printEdge() for x in self.root.edges])


def getAllSuffixes(s):
    res = set()
    for i in range(len(s)):
        res.add(s[i:])
    return res


if __name__ == '__main__':
    s = input()
    root = SuffixTree(s)
    print(root)

    allSuffixes = getAllSuffixes(s)
    treeSuffixes = root.getAllSuffixes()
