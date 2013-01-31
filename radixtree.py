from tree import Tree

class RadixData:
    def __init__(self, key = '', real = False, value = None):
        self.key = key
        self.real = real
        self.value = value

    def getKey(self):
        return self.key

    def isReal(self):
        return self.real

    def setReal(self, real):
        self.real = real

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def __str__(self):
        return '%s%s%s' % (self.key, '*' if self.real else '', '{%s}' % str(self.value) if self.value else '')

class RadixTree:
    def __init__(self):
        self.root = Tree(RadixData())
        self.size = 0

    def getRoot(self):
        return self.root

    def insert(self, key, value, merge=None, replicate=None):
        try:
            self._insert(key, self.root, value, merge, replicate)
        except Exception:
            raise Exception('Duplicate key ' + key)
        self.size += 1

    def _insert(self, key, node, value, merge, replicate):
        keyLen = len(key)
        nodeData = node.getData()
        nodeKey = nodeData.getKey()
        nodeLen = len(nodeKey)
        i = 0
        while i < keyLen and i < nodeLen:
            if key[i] != nodeKey[i]:
                break
            i += 1

        # we are either at the root node or we need to go down the tree
        if nodeLen == 0 or i == 0 or keyLen > i >= nodeLen:
            flag = False
            newText = key[i:keyLen]
            if node.hasChildren():
                for child in node.getChildren():
                    if child.getData().getKey().startswith(newText[0]):
                        flag = True
                        self._insert(newText, child, value, merge, replicate)
                        break

            # just add the node as the child of the current node
            if not flag:
                node.add(RadixData(newText, True, value))
        # there is a exact match just make the current node as data node
        elif i == keyLen and i == nodeLen:
            if nodeData.isReal():
                if not merge:
                    raise Exception('Duplicate key')
                else:
                    merge(nodeData, value)
            else:
                nodeData.setReal(True)
                nodeData.setValue(value)
        # This node need to be split as the key to be inserted is a prefix of the current node key
        elif 0 < i < nodeLen:
            nl = Tree(RadixData(nodeKey[i:nodeLen], nodeData.isReal(), nodeData.getValue()))
            node.moveChildrenTo(nl)
            nodeData.setKey(key[0:i])
            nodeData.setReal(False)
            node.add(nl) # note: node's value is now also in its child.

            if i < keyLen:
                node.add(RadixData(key[i:keyLen], True, value))
                if replicate:
                    nodeData.setValue(replicate(nodeData.getValue()))
            # else node's value is referenced in both self and child.
            else:
                nodeData.setValue(value)
                nodeData.setReal(True)
        # This key need to be added as the child of the current node
        else:
            node.add(RadixData(nodeKey[i:nodeLen], nodeData.isReal(), nodeData.getValue()))
            nodeData.setKey(key)
            nodeData.setReal(True)
            nodeData.setValue(value)

    def __str__(self):
        return str(self.root)


tree = RadixTree()
string = 'banana'
for i in range(0, 3):
    print string[i:]
    tree.insert(string[i:], 1)
print tree