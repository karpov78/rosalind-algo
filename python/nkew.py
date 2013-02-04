class Node:
    def __init__(self, value=None):
        self.value = value
        self.parentEdge = None
        self.edges = []

    def toString(self, indent=''):
        result = indent + (self.value if self.value else "@") + (
            '' if not self.parentEdge else (' (%d)' % self.parentEdge.weight))
        for e in self.edges:
            result += '\n' + e.end.toString('\t' + indent)
        return result


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight
        self.start.edges.append(self)
        self.end.parentEdge = self


class Tree:
    def __init__(self):
        self.root = Node()
        self.namedNodes = {}
        self.internalEdges = []

    def add(self, parent, value, weight):
        node = Node(value)
        self.namedNodes[value] = node
        Edge(parent, node, weight)

    def addRoot(self, parent):
        node = Node()
        edge = Edge(parent, node, 0)
        self.internalEdges.append(edge)
        return node

    def getValues(self):
        return list(sorted(self.namedNodes.keys()))

    def getNode(self, value):
        return self.namedNodes[value]

    def __str__(self):
        return self.root.toString()


def parseTree(s):
    res = Tree()

    bTerm = True
    term = ''
    weight = ''
    nodes = []

    for i in range(len(s)):
        c = s[i]
        if c == '(':
            if len(nodes) == 0:
                nodes.append(res.root)
            else:
                nodes.append(res.addRoot(nodes[-1]))
        elif c == ')':
            if len(term) > 0:
                res.add(nodes[-1], term, int(weight))
            elif len(weight) > 0:
                nodes[-1].parentEdge.weight = int(weight)
                nodes.pop() # move up after applying parent weight
            if s[i + 1] != ':': # look ahead for parent weight
                nodes.pop()
            term = ''
            weight = ''
            bTerm = True
        elif c == ',':
            if len(term) > 0:
                res.add(nodes[-1], term, int(weight))
            elif len(weight) > 0:
                nodes[-1].parentEdge.weight = int(weight)
                nodes.pop() # move up after applying parent weight
            term = ''
            weight = ''
            bTerm = True
        elif c == ';':
            break
        elif c == ':':
            bTerm = False
        else:
            if bTerm:
                term += c
            else:
                weight += c
    return res


def traverse(node, target, path=None):
    if not path: path = []

    if node == target:
        return sum([e.weight for e in path])
    for e in node.edges:
        if not e in path:
            value = traverse(e.end, target, path + [e])
            if value: return value
    if not node.parentEdge in path:
        value = traverse(node.parentEdge.start, target, path + [node.parentEdge])
        if value: return value
    return 0

if __name__ == '__main__':
    result = []
    while True:
        s = input()
        if not s: break
        start, end = input().split(' ')
        input()
        tree = parseTree(s)

        startNode = tree.getNode(start)
        endNode = tree.getNode(end)
        result.append(str(traverse(startNode, endNode)))
    print(' '.join(result))
    #print(parseTree(input()))