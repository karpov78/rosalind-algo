class Node:
    def __init__(self, value=None):
        self.value = value
        self.edges = []

    def toString(self, indent=''):
        result = indent + (self.value if self.value else "@")
        for e in self.edges:
            result += '\n' + e.toString('\t' + indent)
        return result


class Tree:
    def __init__(self):
        self.root = Node()
        self.namedNodes = {}
        self.internalEdges = []

    def add(self, parent, value):
        node = Node(value)
        self.namedNodes[value] = node
        parent.edges.append(node)

    def addRoot(self, parent):
        node = Node()
        parent.edges.append(node)
        self.internalEdges.append((parent, node))
        return node

    def getValues(self):
        return list(sorted(self.namedNodes.keys()))

    def __str__(self):
        return self.root.toString()


def parseTree(s):
    res = Tree()

    term = ''
    nodes = []
    for c in s:
        if c == '(':
            if len(nodes) == 0:
                nodes.append(res.root)
            else:
                nodes.append(res.addRoot(nodes[-1]))
        elif c == ')':
            if len(term) > 0:
                res.add(nodes[-1], term)
                term = ''
            nodes.pop()
        elif c == ',':
            if len(term) > 0:
                res.add(nodes[-1], term)
                term = ''
        elif c == ';':
            break
        else:
            term += c

    return res


def traverseNode(values, row, node, hit_value):
    if node.value:
        row[values.index(node.value)] = hit_value
    else:
        for e in node.edges:
            traverseNode(values, row, e, hit_value)


def createCharTable(tree):
    values = tree.getValues()
    result = set()
    for int_edge in tree.internalEdges:
        row = ['0'] * len(values)
        traverseNode(values, row, int_edge[1], '1')
        #if '@' in row: raise Exception('Invalid row %s' % ''.join(row))
        result.add(''.join(row))
    return result


if __name__ == '__main__':
    s = input()
    tree = parseTree(s)
    values = tree.getValues()
    print(' '.join(values))
    print('\n'.join(createCharTable(tree)))
