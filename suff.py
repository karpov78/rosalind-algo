TERMINAL = '*'
__author__ = 'ekarpov'

class Edge:
    def __init__(self, s, e, value):
        self.value = value
        self.s = s
        self.e = e

    def split(self, position):
        splitValue = self.value[position:]
        result = self.e.addCopyChildren(splitValue) if len(splitValue) > 0 else self
        self.value = self.value[:position]
        return result

    def printEdge(self, indent=''):
        res = indent + self.value
        for c in self.e.edges:
            res += '\n' + c.printEdge('\t' + indent)
        return res


class Node:
    def __init__(self):
        self.edges = []

    def add(self, value):
        for e in self.edges:
            if e.value[0] == value:
                return e
        self.edges.append(Edge(self, Node(), value))
        return self.edges[-1]

    def addCopyChildren(self, value):
        for e in self.edges:
            if e.value[0] == value:
                raise Exception("....")
        newNode = Node()
        newNode.edges = self.edges
        for e in self.edges: e.s = newNode
        self.edges = [Edge(self, newNode, value)]
        return self.edges[-1]


class Marker:
    def __init__(self, edge):
        self.edge = edge
        self.position = 0

    def next(self, s):
        if len(self.edge.value) > self.position + 1:
            self.position += 1
            return self.edge.value[self.position] == s
        elif len(self.edge.e.edges) == 0:
            self.edge.value += s
            self.position += 1
            return True
        else:
            for sub in self.edge.e.edges:
                if sub.value[0] == s:
                    self.edge = sub
                    self.position = 0
                    return True
            return False


class SuffixTree:
    def __init__(self):
        self.root = Node()
        self.markers = []

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
        marker.edge = marker.edge.e.add(s)
        marker.position = 0

        for m in self.markers:
            if m.edge == oldEdge and m.position >= oldPosition:
                m.edge = newEdge
                m.position = m.position - oldPosition


    def __str__(self):
        return '\n'.join([x.printEdge() for x in self.root.edges])


class GraphNode:
    def __init__(self, value=None, parent=None):
        if not value: # root node
            self.value = ["ROOT"]
            self.children = []
            self.parent = None
            self.hasTerminal = False
        else:
            self.value = value
            self.children = []
            self.parent = parent
            self.hasTerminal = True

    def append(self, symbol):
        startsWith = False
        if len(self.children):
            for c in self.children[:]:
                startsWith = startsWith or c.value[0] == symbol
                c.append(symbol)

        if not self.parent:
            if not startsWith:
                self.add([symbol, TERMINAL])
            return

        i = len(self.value) - 1
        while i >= 0:
            if self.value[i] == TERMINAL:
                self.hasTerminal = True
                if i + 1 == len(self.value):
                    if len(self.children) == 0: # no children append here
                        self.value[i] = symbol
                        self.value.append(TERMINAL)
                    elif startsWith: # propagate to children
                        del self.value[i]
                        for c in self.children:
                            if c.value[0] == symbol:
                                c.value.insert(1, TERMINAL)
                                break
                    else: # create a new node
                        del self.value[i]
                        self.add([symbol, TERMINAL])
                elif self.value[i + 1] == symbol:
                    self.value[i] = symbol
                    self.value[i + 1] = TERMINAL
                else:
                    self.add(self.value[i + 1:])
                    self.add([symbol, TERMINAL])
                    self.value = self.value[:i]
                    self.hasTerminal = False
            i -= 1

        if self.value[0] == symbol and self.parent == root:
            self.value.insert(1, TERMINAL)

    def getValue(self):
        return ''.join(self.value)

    def finish(self):
        if self.hasTerminal:
            i = 0
            while i < len(self.value) - 1:
                if self.value[i] == TERMINAL:
                    self.add(self.value[i])
                    self.add(self.value[i + 1:])
                    self.value = self.value[:i]
                i += 1
            if self.value[-1] == TERMINAL and len(self.children) > 0:
                del self.value[-1]
                self.add([TERMINAL])

        for c in self.children:
            c.finish()

    def add(self, value):
        if len(value) > 0:
            for c in self.children:
                if c.value == value:
                    return
            self.children.append(GraphNode(value, self))

    def traverse(self, enter, exit):
        if self.parent: enter(self)
        for c in self.children: c.traverse(enter, exit)
        if self.parent: exit(self)

    def _toString(self, indent=''):
        res = indent + self.getValue()
        for c in self.children:
            res += '\n' + c._toString(indent + '\t')
        return res

    def __str__(self):
        return self._toString()

#root = GraphNode()
root = SuffixTree()
s = input()
for c in s:
    root.append(c)
#root.finish()

print(root)

#def visit(n):
#    print(n.getValue())
#root.traverse(enter=visit, exit=lambda n: n)
#print(TERMINAL)
