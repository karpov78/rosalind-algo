class Tree:
    def __init__(self, data, parent=None, key=lambda x: x):
        self.data = data
        self.children = []
        self.parent = parent
        self.key = key
        self.nodes = {key(data): self}

    def getParent(self):
        return self.parent

    def getData(self):
        return self.data

    def hasChildren(self):
        return len(self.children) > 0

    def getChildren(self):
        return self.children

    def replaceChild(self, childIdx, newNode):
        self.children[childIdx] = newNode
        self._registerNode(newNode)

    def _registerNode(self, newNode):
        self.nodes[self.key(newNode.data)] = newNode
        newNode.parent = self
        if self.parent: self.parent._registerNode(newNode)

    def add(self, node):
        if type(node) is Tree:
            self.children.append(node)
            self._registerNode(node)
            return node
        else:
            newNode = Tree(node, self, key=self.key)
            self.children.append(newNode)
            self._registerNode(newNode)
            return newNode

    def __add__(self, other):
        self.add(other)

    def find(self, key):
        if key in self.nodes:
            return self.nodes[key]
        else:
            print("No node found for key %s" % key)
            raise KeyError(key)

    def __getitem__(self, item):
        return self.find(item)

    def moveChildrenTo(self, tree):
        tree.children = self.children
        for child in tree.children:
            child.parent = tree
        self.children = []

    def getLeaves(self):
        if not self.children:
            return [self]
        else:
            leaves = []
            for child in self.children:
                leaves += child.getLeaves()
            return leaves

    def _print(self, prefix):
        result = prefix + str(self.data)
        for node in self.children:
            result += '\n' + node._print(prefix + '\t')
        return result

    def __str__(self):
        return self._print('')

    def traverse(self, visitor):
        visitor(self)
        for c in self.children:
            c.traverse(visitor)

    def toNewick(self, root=True):
        result = ''
        if len(self.children) > 0:
            result += '(' + ','.join([x.toNewick(False) for x in self.children]) + ')'
        if self.data: result += str(self.data)
        return result + (';' if root else '')

    def getPath(self):
        if self.parent:
            path = self.parent.getPath()
            path.append(self)
            return path
        else:
            return [self]

    def getSize(self):
        return 1 + sum([x.getSize() for x in self.children])
